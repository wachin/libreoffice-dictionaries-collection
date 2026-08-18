#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# package-dicts.sh
#
# Compress each dictionary folder from the third-party submodule into an
# individual .tar.xz archive and place it in the build/ directory.
#
# Usage:
#   cd /path/to/guitarchordstudio
#   bash tools/package-dicts.sh
#
# Output:
#   build/dict-af.tar.xz
#   build/dict-an.tar.xz
#   ...
# ---------------------------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BUILD_DIR="$PROJECT_ROOT/build"
DICTS_DIR="$PROJECT_ROOT/third-party/libreoffice-dictionaries-collection/dicts"

# Check that the source dictionaries exist
if [ ! -d "$DICTS_DIR" ]; then
    echo "ERROR: Dictionary source not found at: $DICTS_DIR"
    echo "Make sure the git submodule is initialized:"
    echo "  git submodule update --init --recursive"
    exit 1
fi

# Create the build directory
mkdir -p "$BUILD_DIR"

# Find all dict-* directories and compress each one
echo "=== Packaging dictionaries into $BUILD_DIR ==="
count=0
for dict_dir in "$DICTS_DIR"/dict-*/; do
    dict_name="$(basename "$dict_dir")"
    archive="$BUILD_DIR/${dict_name}.tar.gz"

    # Skip if the archive already exists and is newer than the source
    if [ -f "$archive" ] && [ "$archive" -nt "$dict_dir" ]; then
        echo "  SKIP $dict_name (already up to date)"
        continue
    fi

    echo "  PACK $dict_name -> ${dict_name}.tar.gz"
    # Use gzip for faster compression (text files compress well)
    tar -czf "$archive" -C "$DICTS_DIR" "$dict_name"
    count=$((count + 1))
done

echo "=== Done! $count dictionaries packaged ==="
echo "Output directory: $BUILD_DIR"
ls -lh "$BUILD_DIR"/*.tar.gz 2>/dev/null | awk '{print "  " $NF " (" $5 ")"}'