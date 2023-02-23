import React, { useRef, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Box, IconButton, Input, Typography, useTheme } from '@mui/material';
import { Sidebar, Menu, MenuItem, useProSidebar } from 'react-pro-sidebar';
import { tokens } from '../theme';

import sidebarItems from './SidebarItems';

import ProfilePic from '../assets/suprapixel.jpg';
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import DashboardOutlinedIcon from '@mui/icons-material/DashboardOutlined';
import GitHubIcon from '@mui/icons-material/GitHub';
import StarIcon from '@mui/icons-material/Star';
import CheckIcon from '@mui/icons-material/Check';
import axiosI from '../api';

const Item = ({ title, to, icon, selected }) => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    return (
        <MenuItem
            active={selected === to}
            style={{ color: colors.grey[100] }}
            // onClick={() => setSelected(title)}
            icon={icon}
            component={<Link to={to}/>}
        >
            <Typography>{title}</Typography>
        </MenuItem>
    )
}

const SideBar = ({ userId, setUserId }) => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const location = useLocation();
    const gitHubRef = useRef();
    const { collapseSidebar, collapsed } = useProSidebar();
    const [ modId, setModId ] = useState(userId);
    const [ mod, setMod ] = useState(false);

    const redirectGithub = () => {
        gitHubRef.current.click();
    }

    const handleSend = async () => {
        try {
            const response = await axiosI(`select_user/${modId}`);
            
            if(typeof(response.data) === 'number') {
                setMod(false);
                if (userId !== modId) {
                    if (modId === '') {
                        setUserId(1);
                    } else {
                        setUserId(modId);
                    }
                }
            }
        } catch (err){
            // console.error(err);
            console.error('El usuario ' + modId + ' no esta disponible para los datos');
            setUserId(1);
        }
    }

    const handleUserId = (e) => {
        e.preventDefault();
        e.stopPropagation();

        const value = e.target.value;
        if((value > 0 && value <= 300) || value === '') {
            setModId(value);
            setMod(true);
        }
    }

    const handleBlur = () => {
        if (modId === '') {
            setModId(1);
            setMod(true);
        }
    }


    return (
        <Box
            display='flex'
            height='100%'
            sx={{
                '& .ps-sidebar-container': {
                    background: `${colors.grey[600]} !important`
                },
                '& .ps-menu-button': {
                    backgroundColor: 'transparent !important',
                    margin: '0.25rem 0'
                },
                '& .pro-inner-item': {
                    padding: '6px 35px 6px 20px !important'
                },
                '& .ps-menu-root ul': {
                    height: '100vh',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '1.5rem'
                }
                ,
                '& .ps-menu-button:hover': {
                    color: `${colors.primary[100]} !important` // #9ca2ff
                },
                '& .ps-menu-button.ps-active': {
                    marginRight: '1.5rem',
                    color: `${colors.grey[100]} !important`, // #6870fa
                    backgroundColor: `${colors.primary[400]} !important`,
                    borderRadius: '0.25rem'
                },
            }}
        >
            <Sidebar style={{ border: 'none', borderRight: `${colors.grey[400]} solid 2px`}} >
                <Menu>
                    <MenuItem
                        // onClick={() => collapseSidebar()}
                        icon={collapsed ? <MenuOutlinedIcon /> : undefined}
                    >
                        {!collapsed && (
                            <Box
                                display="flex"
                                justifyContent="space-between"
                                alignItems="center"
                                ml="0.5rem"
                            >
                                <Typography 
                                    color={colors.grey[100]}
                                    fontSize='20px'
                                    fontWeight='bold'
                                >
                                    Proyecto Humai
                                </Typography>

                                <MenuOutlinedIcon />
                                {/* <IconButton>
                                    <MenuOutlinedIcon />
                                </IconButton> */}
                            </Box>
                        )}
                    </MenuItem>

                    {!collapsed && (
                        <Box m='1.5rem 0 0.25rem'>
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
                            </Box>
                        </Box>
                    )}

                    <Box display='flex' justifyContent='center' alignItems='flex-end' gap='0.75rem'>
                        <Typography>
                            Id usuario:
                        </Typography>
                        <Input
                            // type='number'
                            value={modId}
                            onChange={handleUserId}
                            onBlur={handleBlur}
                            sx={{
                                width: '2.5rem',
                                '& input': {
                                    textAlign: 'center'
                                }
                            }}
                        />
                        <CheckIcon
                            onClick={handleSend}
                            color='secondary'
                            sx={{
                                'opacity': mod ? 1 : 0
                            }}
                        />
                    </Box>

                    {!collapsed && (
                        <Box paddingLeft={collapsed ? undefined : '10%'}>
                            <Item 
                                title='Dashboard'
                                to='/'
                                icon={<DashboardOutlinedIcon />}
                                selected={location.pathname}
                                // setSelected={setSelected}
                            />

                            {sidebarItems.map(section => 
                            <React.Fragment key={section.name}>
                                <Typography
                                    variant="h6"
                                    color={colors.grey[200]}
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
                                        selected={location.pathname}
                                        // setSelected={setSelected}
                                    
                                    />    
                                )}
                            </React.Fragment>
                            )}
                        </Box>
                    )}

                    {!collapsed && (
                    <Box
                        sx={{
                            margin: 'auto 2.5rem 3rem',
                            minHeight: '9rem',
                            p: '16px 0px',
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                            justifyContent: 'center',
                            gap: '2px',

                            backgroundColor: colors.blueAccent[700],
                            borderRadius: '16px'
                        }}
                    >
                        <GitHubIcon sx={{height: '2rem', width: '2rem'}}/>

                        <Typography
                            mt='8px'
                            fontSize='14px'
                            fontWeight='bold'
                            letterSpacing='0.5px'
                            color='#fff'
                        >
                            Te gusto el proyecto?
                        </Typography>

                        <Typography fontSize='13px' color='#FAFAFA'>
                            Mira el repositorio
                        </Typography>

                        <IconButton
                            onClick={redirectGithub}
                            sx={{
                                marginTop: '6px',
                                display: 'flex',
                                // alignItems: 'flex-end',
                                justifyContent: 'center',
                                gap: '0.25rem',
                                backgroundColor: colors.grey[100],
                                color: colors.primary[600],
                                borderRadius: '8px',
                                boxShadow: 'rgba(149, 157, 165, 0.2) 0px 4px 12px;',
                                '&:hover': {
                                    backgroundColor: colors.grey[200]
                                }
                            }}
                        >
                            <StarIcon sx={{color: colors.blueAccent[800]}}/>
                            <Typography>
                                Star
                            </Typography>
                        </IconButton>
                        <a hidden ref={gitHubRef} href='https://github.com/PabloSGomez50/humai-solar-panels' target='_blank'/>
                    </Box>
                    )}
                </Menu>
            </Sidebar>
        </Box>
    )
}

export default SideBar;