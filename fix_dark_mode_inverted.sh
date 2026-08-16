#!/bin/bash
PALETTES="gray mauve slate sage olive sand tomato red ruby crimson pink plum purple violet iris indigo blue cyan teal jade green grass brown bronze gold sky mint lime yellow amber orange"
declare -A INVERSE_MAP=([50]=950 [100]=900 [200]=800 [300]=700 [400]=600 [500]=500 [600]=400 [700]=300 [800]=200 [900]=100 [950]=50)
for palette in $PALETTES; do
  for scale in 50 100 200 300 400 500 600 700 800 900 950; do
    inverse=${INVERSE_MAP[$scale]}
    find src -name "*.tsx" -exec sed -i "s/-${palette}-${scale}/-${palette}Dark-${inverse}/g" {} \;
  done
done
echo "Inversión completada."
