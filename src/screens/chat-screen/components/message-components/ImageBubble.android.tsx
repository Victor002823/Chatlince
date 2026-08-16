import React from 'react';
import { useColorScheme } from 'react-native';
import ImageModal from 'react-native-image-modal';
import { tailwind } from '@/theme';
import { useImageDimensions } from '@/hooks/useImageDimensions';
import type { ImageCellProps, ImageContainerProps } from '@/hooks/useImageDimensions';

export const ImageBubbleContainer = (props: ImageContainerProps) => {
  const { imageSrc, maxWidth = 300, maxHeight = 360 } = props;
  const imageStyle = useImageDimensions(imageSrc, maxWidth, maxHeight);
  const colorScheme = useColorScheme();
  const imageBgColor = tailwind.color(
    colorScheme === 'dark' ? 'bg-grayDark-100' : 'bg-gray-100',
  ) as string;

  return (
    <ImageModal
      source={{ uri: imageSrc }}
      resizeMode="contain"
      modalImageResizeMode="contain"
      overlayBackgroundColor="#000000"
      imageBackgroundColor={imageBgColor}
      isTranslucent
      style={[tailwind.style('bg-gray-100 dark:bg-grayDark-100 overflow-hidden'), imageStyle]}
    />
  );
};

export const ImageBubble = (props: ImageCellProps) => {
  const { imageSrc } = props;

  return (
    <React.Fragment>
      <ImageBubbleContainer {...{ imageSrc }} />
    </React.Fragment>
  );
};
