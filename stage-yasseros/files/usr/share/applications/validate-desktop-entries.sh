#!/bin/bash
# Validate all YasserOS .desktop entries have required fields and valid categories.
set -e

DESKTOP_DIR="$(dirname "$0")"
ERRORS=0

for f in "$DESKTOP_DIR"/yasseros*.desktop "$DESKTOP_DIR"/yasser-control-center.desktop; do
    [ -f "$f" ] || continue
    name=$(basename "$f")

    for field in Name Exec Categories Type; do
        if ! grep -q "^${field}=" "$f"; then
            echo "FAIL [$name]: missing field $field"
            ERRORS=$((ERRORS + 1))
        fi
    done

    cats=$(grep "^Categories=" "$f" | cut -d= -f2)
    if echo "$cats" | grep -q "YasserOS"; then
        echo "OK   [$name]: has YasserOS category"
    else
        echo "WARN [$name]: missing YasserOS category"
    fi
done

if [ "$ERRORS" -gt 0 ]; then
    echo "Validation failed with $ERRORS error(s)."
    exit 1
fi
echo "All desktop entries validated."
