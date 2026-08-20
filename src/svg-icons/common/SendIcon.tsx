import React from 'react';
import Svg, { Path } from 'react-native-svg';
import { useColorScheme } from 'react-native';

export const SendIcon = () => {
  const colorScheme = useColorScheme();
  const strokeColor = colorScheme === 'dark' ? '#171717' : 'white';

  return (
    <Svg width="100%" height="100%" viewBox="0 0 16 16" fill="none">
      <Path
        d="M8 13.3334V2.66675M8 2.66675L4 6.66675M8 2.66675L12 6.66675"
        stroke={strokeColor}
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </Svg>
  );
};
