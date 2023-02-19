import { Box, Typography } from "@mui/material"
import { useEffect, useState } from "react";

import LightModeIcon from '@mui/icons-material/LightMode';
import CloudQueueIcon from '@mui/icons-material/CloudQueue';

const DashClima = ({ clima, colors }) => {

    const [ selected, setSelected ] = useState({});

    useEffect(() => {
        setSelected(clima[0]);
    }, [clima])

    return (
        <Box
            gridColumn='span 4'
            gridRow='span 2'
            p='1.25rem 1rem'
            display='flex'
            flexDirection='column'
            gap='1.25rem'
            backgroundColor={colors.grey[500]}
        >
            <Box display='flex' gap='0.5rem' alignItems='center'>
                {selected && selected.icon ?
                    <CloudQueueIcon sx={{color: colors.secondary[400]}} />
                    :
                    <LightModeIcon sx={{color: colors.secondary[400]}} />
                }
                <Typography
                    variant="h4"
                    fontWeight="600"
                    color={colors.grey[100]}
                >
                    Clima En los proximos 7 dias
                </Typography>
            </Box>

            {clima && selected?.fecha && clima.length > 0 &&
                <Box
                    height='100%'
                    display='flex'
                    // flexDirection='column'
                    gap='0.5rem'
                    // overflow='hidden scroll'
                    backgroundColor={colors.grey[700]}
                    borderRadius='0.75rem'
                >
                    <Box
                        flex='2'
                        p='1rem'
                        display='flex'
                        flexDirection='column'
                        justifyContent='space-between'
                        backgroundColor={colors.blueAccent[400]}
                        borderRadius='0.75rem'
                    >
                        <Box>
                            <Typography fontSize='20px' fontWeight='600'>
                                {selected.dia}
                            </Typography>

                            <Typography>
                                {selected.fecha}
                            </Typography>

                            <Typography>
                                Sidney, Australia
                            </Typography>
                        </Box>

                        <Box>
                            {selected.icon ?
                                <CloudQueueIcon fontSize='large' sx={{color: colors.grey[100]}} />
                                :
                                <LightModeIcon fontSize='large' sx={{color: colors.grey[100]}} />
                            }
                            <Typography fontSize='36px' fontWeight='bold'>
                                {selected.temp} °C
                            </Typography>

                            <Typography fontSize='20px' fontWeight='600'>
                                {selected.clima}
                            </Typography>
                        </Box>
                    </Box>

                    <Box
                        flex='3'
                        display='flex'
                        flexDirection='column'
                        alignItems='center'
                        justifyContent='space-around'
                    >
                        <Box 
                            p='0rem 2rem' 
                            width='100%'
                            sx={{ '& p': { fontSize: '16px' } }}
                        >
                            <Box display='flex' justifyContent='space-between' alignItems='center'>
                                <Typography fontWeight='600'>HUMEDAD:</Typography>
                                <Typography>{selected.humedad} %</Typography>
                            </Box>

                            <Box display='flex' justifyContent='space-between' alignItems='center'>
                                <Typography fontWeight='600'>VIENTO:</Typography>
                                <Typography>{selected.viento} Km/h</Typography>
                            </Box>
                            
                            <Box display='flex' justifyContent='space-between' alignItems='center'>
                                <Typography fontWeight='600'>PRESION:</Typography>
                                <Typography>{selected.presion} hPa</Typography>
                            </Box>

                        </Box>

                        <Box
                            display='flex' 
                            borderRadius='0.5rem'
                            backgroundColor={colors.grey[500]}
                            sx={{'pointer': 'cursor'}}
                        >
                            {clima.map( dia => 
                                <Box
                                    key={dia.fecha}
                                    p='0.5rem 0.625rem'
                                    display='flex' 
                                    flexDirection='column' 
                                    alignItems='center'
                                    gap='0.5rem'
                                    color={selected.fecha === dia.fecha && colors.grey[800]}
                                    backgroundColor={selected.fecha === dia.fecha && colors.grey[200]}
                                    onClick={() => setSelected(dia)}
                                    borderRadius='0.5rem'
                                >
                                    <Typography fontSize='14px'>
                                        {dia.dia.slice(0,3)}
                                    </Typography>
                                    <Typography>
                                        {dia.temp} °C
                                    </Typography>
                                </Box>
                            )}
                        </Box>
                        {/* 
                        <Box>
                            Horas
                        </Box>
                        */}
                    </Box>
                    {/* 
                    {clima.map(item => 
                        <Box
                            key={item.fecha}
                            p='0.75rem 1rem'
                            // backgroundColor={colors.grey[700]}
                            // borderRadius='0.5rem'
                        >
                            <Typography>
                                {item.temp} °C
                            </Typography>
                        </Box>    
                    )} 
                    */}
                </Box>
            }
        </Box>
    )
}

export default DashClima;