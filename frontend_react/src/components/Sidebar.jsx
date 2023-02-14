import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Box, IconButton, Typography, useTheme } from '@mui/material';
import { Sidebar, Menu, MenuItem, useProSidebar } from 'react-pro-sidebar';
import { tokens } from '../theme';

import sidebarItems from './SidebarItems';

import ProfilePic from '../assets/suprapixel.jpg';
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import DashboardOutlinedIcon from '@mui/icons-material/DashboardOutlined';

const Item = ({ title, to, icon, selected, setSelected }) => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    return (
        <MenuItem
            active={selected === title}
            style={{ color: colors.grey[100] }}
            onClick={() => setSelected(title)}
            icon={icon}
            component={<Link to={to}/>}
        >
            <Typography>{title}</Typography>
        </MenuItem>
    )
}

const SideBar = () => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const [selected, setSelected] = useState('Dashboard');

    const { collapseSidebar, collapsed } = useProSidebar(); 


    return (
        <Box
            sx={{
                display: 'flex',
                height: '100%',
                '& .ps-sidebar-container': {
                    background: `${colors.primary[400]} !important`
                },
                '& .ps-menu-button': {
                    backgroundColor: 'transparent !important',
                },
                '& .pro-inner-item': {
                    padding: '6px 35px 6px 20px !important'
                },
                '& .ps-menu-root ul': {
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '1.5rem'
                }
                ,
                '& .ps-menu-button:hover': {
                    color: '#9ca2ff !important'
                },
                '& .ps-menu-button.ps-active': {
                    color: '#6870fa !important'
                },
            }}
        >
            <Sidebar style={{ border: 'none'}} >
                <Menu>
                    <MenuItem
                        onClick={() => collapseSidebar()}
                        icon={collapsed ? <MenuOutlinedIcon /> : undefined}
                    >
                        {!collapsed && (
                            <Box
                                display="flex"
                                justifyContent="space-between"
                                alignItems="center"
                                ml="0.5rem"
                            >
                                <Typography variant="h4" color={colors.grey[100]}>
                                    Proyecto Humai
                                </Typography>

                                <IconButton>
                                    <MenuOutlinedIcon />
                                </IconButton>
                            </Box>
                        )}
                    </MenuItem>

                    {!collapsed && (
                        <Box mb='1.5rem'>
                            <Box display='flex' justifyContent='center' alignItems='center'>
                                <img
                                    alt='profile-user'
                                    width='80px'
                                    height='80px'
                                    src={ProfilePic}
                                    style={{ cursor: 'pointer', borderRadius: '50%' }}
                                />
                            </Box>

                            <Box textAlign='center'>
                                <Typography
                                    variant='h2'
                                    color={colors.grey[100]}
                                    fontWeight='bold'
                                    sx={{ mt: '0.75rem' }}
                                >
                                    Pablo Gomez
                                </Typography>
                                {/* <Typography

                                >
                                    Full Stack dev
                                </Typography> */}
                            </Box>
                        </Box>
                    )}

                    {!collapsed && (
                        <Box paddingLeft={collapsed ? undefined : '10%'}>
                            <Item 
                                title='Dashboard'
                                to='/'
                                icon={<DashboardOutlinedIcon />}
                                selected={selected}
                                setSelected={setSelected}
                            />

                            {sidebarItems.map(section => 
                            <React.Fragment key={section.name}>
                                <Typography
                                    variant="h6"
                                    color={colors.grey[300]}
                                    sx={{ m: "15px 0 5px 20px" }}
                                >
                                    {section.name}
                                </Typography>
                                {section.data.map(item => 
                                    <Item
                                        key={item.title}
                                        title={item.title}
                                        to={item.to}
                                        icon={<item.icon />}
                                        selected={selected}
                                        setSelected={setSelected}
                                    
                                    />    
                                )}
                            </React.Fragment>
                            )}
                        </Box>
                    )}
                </Menu>
            </Sidebar>
        </Box>
    )
}

export default SideBar;