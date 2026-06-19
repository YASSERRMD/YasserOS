#!/bin/bash
# YasserOS image artifact validation script
# Run after pi-gen build to verify the produced image meets requirements
set -e

BLUE='\033[38;2;68;147;248m'
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m'

DEPLOY_DIR="${1:-$(pwd)/deploy}"
BUDGET_FILE="$(dirname "$(readlink -f "$0")")/../stage-yasseros/performance-budget.json"

ERRORS=0
WARNINGS=0

pass() { echo -e "${GREEN}PASS${NC} $1"; }
fail() { echo -e "${RED}FAIL${NC} $1"; ERRORS=$((ERRORS+1)); }
warn() { echo -e "${YELLOW}WARN${NC} $1"; WARNINGS=$((WARNINGS+1)); }

echo -e "${BLUE}YasserOS Image Validation${NC}"
echo "Deploy dir: $DEPLOY_DIR"
echo "--------------------------"

# Check deploy dir exists
if [ ! -d "$DEPLOY_DIR" ]; then
    fail "Deploy directory not found: $DEPLOY_DIR"
    exit 1
fi

# Find image file
IMG=$(find "$DEPLOY_DIR" -name "*.img" -o -name "*.img.xz" 2>/dev/null | head -1)
if [ -z "$IMG" ]; then
    fail "No .img or .img.xz found in $DEPLOY_DIR"
    exit 1
fi
pass "Image found: $(basename "$IMG")"

# Check image size
MAX_MB=3500
if command -v python3 >/dev/null 2>&1 && [ -f "$BUDGET_FILE" ]; then
    MAX_MB=$(python3 -c "import json; b=json.load(open('$BUDGET_FILE')); print(b['image']['max_size_mb'])")
fi

IMG_SIZE_MB=$(du -m "$IMG" | cut -f1)
if [ "$IMG_SIZE_MB" -le "$MAX_MB" ]; then
    pass "Image size: ${IMG_SIZE_MB}MB (budget: ${MAX_MB}MB)"
else
    fail "Image size ${IMG_SIZE_MB}MB exceeds budget ${MAX_MB}MB"
fi

# Check for SHA256 checksum
SHA_FILE="${IMG}.sha256"
if [ -f "$SHA_FILE" ]; then
    pass "SHA256 checksum present"
    if sha256sum -c "$SHA_FILE" --quiet 2>/dev/null; then
        pass "SHA256 checksum valid"
    else
        fail "SHA256 checksum mismatch"
    fi
else
    warn "No .sha256 file found — generate with: sha256sum $IMG > ${IMG}.sha256"
fi

echo "--------------------------"
if [ "$ERRORS" -gt 0 ]; then
    echo -e "${RED}Validation FAILED: $ERRORS error(s), $WARNINGS warning(s)${NC}"
    exit 1
fi
echo -e "${GREEN}Validation PASSED: 0 errors, $WARNINGS warning(s)${NC}"
