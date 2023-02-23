import { Box, IconButton, useTheme } from "@mui/material";
import { useContext, useRef } from "react";
import { ColorModeContext, tokens } from "../theme";
import { useNavigate } from 'react-router-dom';

import { InputBase } from "@mui/material";
import LightModeOutlinedIcon from '@mui/icons-material/LightModeOutlined';
import DarkModeOutlinedIcon from '@mui/icons-material/DarkModeOutlined';
import NotificationsOutlinedIcon from '@mui/icons-material/NotificationsOutlined';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import PersonOutlinedIcon from '@mui/icons-material/PersonOutlined';
import SearchIcon from '@mui/icons-material/Search';
import Clock from "./Clock";


const TopBar = () => {
    const theme = useTheme();

    const colors = tokens(theme.palette.mode);
    const colorMode = useContext(ColorModeContext);

    const navigate = useNavigate();
    const instagramRef = useRef();

    return (
        <Box 
            display='flex' 
            justifyContent='space-between' 
            backgroundColor={colors.grey[600]}
            borderBottom={`${colors.grey[400]} solid 2px`}
            p={2}
        >

            {/* <Box 
                display='flex' 
                backgroundColor={colors.primary[600]}
                borderRadius='0.25rem'
            >
                <InputBase sx={{ml: 2, flex: 1}} placeholder='Search' />
                <IconButton type="button" sx={{ p: 1 }}>
                    <SearchIcon />
                </IconButton>
            </Box> */}
            <Clock colors={colors}/>
            
            <Box display='flex' >
                <IconButton onClick={colorMode.toggleColorMode}>
                    {theme.palette.mode === 'dark' ?
                        <DarkModeOutlinedIcon />
                    :
                        <LightModeOutlinedIcon />
                    }
                </IconButton>

                {/* <IconButton>
                    <NotificationsOutlinedIcon />
                </IconButton> */}

                {/* <IconButton onClick={() => navigate('/settings')}>
                    <SettingsOutlinedIcon />
                </IconButton> */}

                <IconButton onClick={() => instagramRef.current.click()}>
                    <PersonOutlinedIcon />
                </IconButton>
                <a hidden href='https://github.com/PabloSGomez50' target='_blank' ref={instagramRef}/>
            </Box>
        </Box>
    )
}

export default TopBar;