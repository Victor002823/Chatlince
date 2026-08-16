#!/bin/bash
set -e
cd "$(dirname "$0")"
PALETTES="gray mauve slate sage olive sand tomato red ruby crimson pink plum purple violet iris indigo blue cyan teal jade green grass brown bronze gold sky mint lime yellow amber orange"
SEDEXPR=()
for name in $PALETTES; do
  SEDEXPR+=(-e "s/-${name}-/-${name}Dark-/g")
done
find src -name "*.tsx" -exec sed -i "${SEDEXPR[@]}" {} \;
find src -name "*.tsx" -exec sed -i \
  -e 's/\bbg-white\b/bg-grayDark-50/g' \
  -e 's/\btext-black\b/text-grayDark-950/g' \
  {} \;
echo "Listo."
