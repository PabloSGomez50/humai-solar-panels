import { createContext, useState, useMemo } from "react";
import { createTheme } from '@mui/material/styles';

const dark_default = {
    grey: {
        100: "#e0e0e0",
        200: "#c2c2c2",
        300: "#a3a3a3",
        400: "#858585",
        500: "#666666",
        600: "#525252",
        700: "#3d3d3d",
        800: "#292929",
        900: "#141414"
    },
    primary: {
        100: "#d0d1d5",
        200: "#a1a4ab",
        300: "#727681",
        400: "#1f2a40",
        500: "#141b2d",
        600: "#101624",
        700: "#0c101b",
        800: "#080b12",
        900: "#040509"
    },
    secondary: {
        100: "#dbf5ee",
        200: "#b7ebde",
        300: "#94e2cd",
        400: "#70d8bd",
        500: "#4cceac",
        600: "#3da58a",
        700: "#2e7c67",
        800: "#1e5245",
        900: "#0f2922"
    },
    redAccent: {
        100: "#f8dcdb",
        200: "#f1b9b7",
        300: "#e99592",
        400: "#e2726e",
        500: "#db4f4a",
        600: "#af3f3b",
        700: "#832f2c",
        800: "#58201e",
        900: "#2c100f"
    },
    blueAccent: {
        100: "#e1e2fe",
        200: "#c3c6fd",
        300: "#a4a9fc",
        400: "#868dfb",
        500: "#6870fa",
        600: "#535ac8",
        700: "#3e4396",
        800: "#2a2d64",
        900: "#151632"
    },
}

const test1 = {
    grey: {
        100: "#f6f6f7",
        200: "#edeeef",
        300: "#e7e8e9",
        400: "#e1e2e4",
        500: "#cbcbcd",
        600: "#b4b5b6",
        700: "#878889",
        800: "#5a5a5b",
        900: "#181719"
    },
    primary: {
        100: "#aeb0f7",
        200: "#8e90f4",
        300: "#7d80f2",
        400: "#5d60ef",
        500: "#4143a7",
        600: "#383a8f",
        700: "#252660",
        800: "#131330",
        900: "#131220"
    },
    secondary: {
        100: "#dbf5ee",
        200: "#b7ebde",
        300: "#94e2cd",
        400: "#70d8bd",
        500: "#4cceac",
        600: "#3da58a",
        700: "#2e7c67",
        800: "#1e5245",
        900: "#0f2922"
    },
    redAccent: {
        100: "#f8dcdb",
        200: "#f1b9b7",
        300: "#e99592",
        400: "#e2726e",
        500: "#db4f4a",
        600: "#af3f3b",
        700: "#832f2c",
        800: "#58201e",
        900: "#2c100f"
    },
    blueAccent: {
        100: "#e1e2fe",
        200: "#c3c6fd",
        300: "#a4a9fc",
        400: "#868dfb",
        500: "#6870fa",
        600: "#535ac8",
        700: "#3e4396",
        800: "#2a2d64",
        900: "#151632"
    },
}

export const tokens = (mode) => ({
    ...(mode === 'dark' ?
        {
            grey: {
                100: "#F3F5F7",
                200: "#CED5DF",
                300: "#303B4A", // Changed
                400: "#1B2129", // Changed
                500: "#151C28", // Changed
                600: "#0E141C", // Changed
                700: "#0E121B", // Changed
                800: "#050910", // Changed
                900: "#07090D" // Changed
            },
            primary: {
                100: "#aeb0f7",
                200: "#8e90f4",
                300: "#7d80f2",
                400: "#5d60ef",
                500: "#4143a7",
                600: "#383a8f",
                700: "#252660",
                800: "#131330",
                900: "#131220"
            },
            secondary: {
                100: "#87FDE3",
                200: "#5FFCDA",
                300: "#37FBD0",
                400: "#0FFAC7",
                500: "#04DCAD",
                600: "#03A683",
                700: "#03A07E",
                800: "#02785E",
                900: "#02503F"
            },
            blueAccent: {
                100: "#e1e2fe",
                200: "#c3c6fd",
                300: "#a4a9fc",
                400: "#868dfb",
                500: "#6870fa",
                600: "#535ac8",
                700: "#3e4396",
                800: "#2a2d64",
                900: "#151632"
            },
        }
        :
        {
            grey: {
                900: "#e0e0e0",
                800: "#c2c2c2",
                700: "#a3a3a3",
                600: "#858585",
                500: "#666666",
                400: "#525252",
                300: "#3d3d3d",
                200: "#292929",
                100: "#141414"
            },
            primary: {
                900: "#d0d1d5",
                800: "#a1a4ab",
                700: "#727681",
                600: "#434957",
                500: "#141b2d",
                400: "#f2f0f0",
                300: "#0c101b",
                200: "#080b12",
                100: "#040509"
            },
            secondary: {
                900: "#dbf5ee",
                800: "#b7ebde",
                700: "#94e2cd",
                600: "#70d8bd",
                500: "#4cceac",
                400: "#3da58a",
                300: "#2e7c67",
                200: "#1e5245",
                100: "#0f2922"
            },
            redAccent: {
                900: "#f8dcdb",
                800: "#f1b9b7",
                700: "#e99592",
                600: "#e2726e",
                500: "#db4f4a",
                400: "#af3f3b",
                300: "#832f2c",
                200: "#58201e",
                100: "#2c100f"
            },
            blueAccent: {
                900: "#e1e2fe",
                800: "#c3c6fd",
                700: "#a4a9fc",
                600: "#868dfb",
                500: "#6870fa",
                400: "#535ac8",
                300: "#3e4396",
                200: "#2a2d64",
                100: "#151632"
            },
        }
    )
});

// mui theme settings

export const themeSettings = (mode) => {
    const colors = tokens(mode);

    return {
        palette: {
            mode: mode,
            ...(mode === 'dark' ?
                {
                    primary: {
                        main: colors.primary[500],
                    },
                    secondary: {
                        main: colors.secondary[500],
                    },
                    neutral: {
                        dark: colors.grey[700],
                        main: colors.grey[500],
                        light: colors.grey[100],
                    },
                    background: {
                        default: colors.primary[500],
                    }
                }
                :
                {
                    primary: {
                        main: colors.primary[100],
                    },
                    secondary: {
                        main: colors.secondary[500],
                    },
                    neutral: {
                        dark: colors.grey[700],
                        main: colors.grey[500],
                        light: colors.grey[100],
                    },
                    background: {
                        default: '#fcfcfc',
                    }
                }
            ) 
        },
        typography: {
            fontFamily: ['Source Sans Pro', 'sans-serif'].join(','),
            fontSize: 12,
            h1: {
                fontFamily: ['Source Sans Pro', 'sans-serif'].join(','),
                fontSize: 40,
            },
            h2: {
                fontFamily: ['Source Sans Pro', 'sans-serif'].join(','),
                fontSize: 32,
            },
            h3: {
                fontFamily: ['Source Sans Pro', 'sans-serif'].join(','),
                fontSize: 24,
            },
            h4: {
                fontFamily: ['Source Sans Pro', 'sans-serif'].join(','),
                fontSize: 20,
            },
            h5: {
                fontFamily: ['Source Sans Pro', 'sans-serif'].join(','),
                fontSize: 16,
            },
            h6: {
                fontFamily: ['Source Sans Pro', 'sans-serif'].join(','),
                fontSize: 14,
            },
        }
    }
};

export const ColorModeContext = createContext({
    toggleColorMode: () => {

    }
});

export const useMode = () => {
    const [mode, setMode] = useState('dark');

    const colorMode = useMemo(() => ({
        toggleColorMode: () => setMode(prev => (prev === 'light' ? 'dark' : 'light'))
    }), []);

    const theme = useMemo(() => createTheme(themeSettings(mode)), [mode]);

    return [theme, colorMode];
}