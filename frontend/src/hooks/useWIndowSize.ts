import { useLayoutEffect, useState } from "react";

const useWindowSize = (): number => {
  const windowResize = (): void => {
    setWindowSize(window.innerWidth);
  };

  const [windowSize, setWindowSize] = useState<number>(window.innerWidth);
  useLayoutEffect(() => {
    window.addEventListener("resize", windowResize);
    return () => window.removeEventListener("resize", windowResize);
  });
  return windowSize;
};

export default useWindowSize;
