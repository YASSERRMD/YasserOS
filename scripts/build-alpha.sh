#!/bin/bash
# YasserOS alpha image build script
# Wrapper around pi-gen Docker build using the default build profile
set -e

REPO_ROOT="$(dirname "$(readlink -f "$0")")/.."
cd "$REPO_ROOT"

BLUE='\033[38;2;68;147;248m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}YasserOS Alpha Image Build${NC}"
echo "----------------------------"

# Load default build profile
PROFILE="${PROFILE:-build-profiles/default.conf}"
if [ ! -f "$PROFILE" ]; then
    echo -e "${RED}Build profile not found: $PROFILE${NC}"
    exit 1
fi
# shellcheck source=/dev/null
source "$PROFILE"
echo "Profile: $PROFILE (IMG_NAME=$IMG_NAME)"

# Check for pi-gen
PIGEN_DIR="${PIGEN_DIR:-../pi-gen}"
if [ ! -d "$PIGEN_DIR" ]; then
    echo -e "${RED}pi-gen not found at: $PIGEN_DIR${NC}"
    echo "Clone it with: git clone https://github.com/RPi-Distro/pi-gen.git ../pi-gen"
    exit 1
fi

# Ensure stage-yasseros is linked
STAGE_LINK="$PIGEN_DIR/stage-yasseros"
if [ ! -L "$STAGE_LINK" ] && [ ! -d "$STAGE_LINK" ]; then
    echo "Linking stage-yasseros into pi-gen..."
    ln -s "$(pwd)/stage-yasseros" "$STAGE_LINK"
fi

# Create SKIP files for stages we don't want
for stage in stage3 stage4 stage5; do
    touch "$PIGEN_DIR/$stage/SKIP" 2>/dev/null || true
done

# Write config
CONFIG_FILE="$PIGEN_DIR/config"
cat > "$CONFIG_FILE" << EOF
IMG_NAME="$IMG_NAME"
RELEASE="$RELEASE"
TARGET_HOSTNAME="$TARGET_HOSTNAME"
FIRST_USER_NAME="$FIRST_USER_NAME"
TIMEZONE_DEFAULT="$TIMEZONE_DEFAULT"
LOCALE_DEFAULT="$LOCALE_DEFAULT"
KEYBOARD_KEYMAP="$KEYBOARD_KEYMAP"
KEYBOARD_LAYOUT="$KEYBOARD_LAYOUT"
GPU_MEM=$GPU_MEM
ENABLE_SSH=${ENABLE_SSH:-0}
DEPLOY_ZIP=${DEPLOY_ZIP:-1}
EOF

echo "Config written to $CONFIG_FILE"
echo -e "${BLUE}Starting pi-gen Docker build...${NC}"

cd "$PIGEN_DIR"
./build-docker.sh

echo -e "${GREEN}Build complete. Image in $PIGEN_DIR/deploy/${NC}"

# Validate the image
cd "$REPO_ROOT"
if [ -x scripts/validate-image.sh ]; then
    bash scripts/validate-image.sh "$PIGEN_DIR/deploy"
fi
