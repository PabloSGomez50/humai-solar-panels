import { Box, Button, IconButton, useTheme, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import { tokens } from '../theme';
import Header from "../components/Header";
import axios from 'axios';

import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import ElectricBoltIcon from '@mui/icons-material/ElectricBolt';
import SolarPowerIcon from '@mui/icons-material/SolarPower';

import EmailIcon from "@mui/icons-material/Email";
import StatBox from "../components/StatBox";
import LineChart from "./Graficos/Line";
import Calendar from "./Graficos/Calendar";
import BarChart from "./Graficos/Bar";

const Dashboard = () => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [ daily, setDaily ] = useState([]);
    const [ barData, setbarData ] = useState({});
    const [ calendarData, setCalendarData ] = useState([]);
    const [ lineData, setLineData ] = useState([]);

    const stats = [
        // {
        //     title: 'Promedio diario',
        //     subtitle: 'En los ultimos 7 dias',
        //     progress: 0.75,
        //     increase: 14,
        //     icon:
        //     <EmailIcon
        //         sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
        //     />
        // },
        // {
        //     title: 'Hora de mayor produccion',
        //     subtitle: 'En los ultimos 7 dias',
        //     progress: 0.33,
        //     increase: 14,
        //     icon:
        //     <EmailIcon
        //         sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
        //     />
        // },
        {
            title: 'Desvio estandar',
            subtitle: 'En los ultimos 7 dias',
            progress: 0.5,
            increase: 14,
            icon:
            <EmailIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
            />
        },
    ]

    useEffect(() => {
        const requestConsumo = async () => {
            const response = await axios(
                'http://127.0.0.1:8000/consumo'
            )

            setDaily(response.data);
        }

        const requestProdCards = async () => {
            const response = await axios(
                'http://127.0.0.1:8000/cards'
            )
            // console.log(response.data);
            setbarData(response.data);
        }

        const requestProdCalendar = async () => {
            const response = await axios(
                'http://127.0.0.1:8000/prod'
            )

            console.log(response.data);
            setCalendarData(response.data);
        }

        const requestRendimiento = async () => {
            const response = await axios(
                'http://127.0.0.1:8000/months'
            )
            
            // console.log(response.data);
            setLineData(response.data);
        }

        requestProdCards();
        requestConsumo();
        requestProdCalendar();
        requestRendimiento();
    }, [])

    return (
        <Box m='1.25rem'>
            <Box display='flex' justifyContent='space-between' alignItems='center'>
                <Header title='DASHBOARD' subtitle='Este es el resumen de tu sistema'/>

                <Button
                    sx={{
                        backgroundColor: colors.blueAccent[700],
                        color: colors.grey[100],
                        fontSize: "14px",
                        fontWeight: "bold",
                        padding: "0.625rem 1.25rem",
                        '&:hover': {backgroundColor: colors.blueAccent[500]}
                    }}
                >
                    <DownloadOutlinedIcon sx={{ mr: "0.625rem" }} />
                    Descargar resumen
                </Button>
            </Box>

            <Box
                display="grid"
                gridTemplateColumns="repeat(12, 1fr)"
                gridAutoRows="105px"
                gap="1.25rem"
                m='1rem'
            >
                {/* 1ra fila 1er columna */}
                <Box
                    gridColumn='span 4'
                    gridRow='span 2'
                    backgroundColor={colors.primary[400]}
                    display='flex'
                    flexDirection='column'
                    p='0.75rem'
                >
                    <Box display='flex' gap='0.5rem'>
                        <ElectricBoltIcon sx={{color: colors.greenAccent[500]}} />
                        <Typography
                            variant="h4"
                            fontWeight="bold"
                            mb='0.75rem'
                            sx={{ color: colors.grey[100] }}
                        >
                            Consumo Total
                        </Typography>
                    </Box>

                    <Box
                        display='flex'
                        height='90%'
                        flexDirection='column'
                        gap='0.5rem'
                        flexWrap='wrap'
                    >
                        {daily.map(item =>
                            <Box
                                key={item.day}
                                display='flex'
                                justifyContent='space-between'
                                p='0 0.5rem'
                            >
                                <Typography sx={{ color: colors.greenAccent[500] }}>
                                    {item.day}
                                </Typography>

                                <Typography sx={{ color: colors.grey[200] }}>
                                    {item.value} Kw
                                </Typography>
                            </Box>
                        )}
                    </Box>
                </Box>

                {/* 1ra fila 2er columna */}
                <Box
                    gridColumn='span 4'
                    gridRow='span 2'
                    backgroundColor={colors.primary[400]}
                    display='flex'
                    flexDirection='column'
                    p='0.75rem'
                >
                    <Box display='flex' gap='0.5rem'>
                        <ElectricBoltIcon sx={{color: colors.greenAccent[500]}} />
                        <Typography
                            variant="h4"
                            fontWeight="bold"
                            mb='0.5rem'
                            sx={{ color: colors.grey[100] }}
                        >
                            Promedio produccion diaria
                        </Typography>
                    </Box>

                    <BarChart 
                        data={barData.prom}
                        keys={['promedio']}
                        indexBy={'dia'}
                    />
                </Box>

                {/* 1ra fila 3er columna */}
                <Box
                    gridColumn='span 4'
                    gridRow='span 2'
                    backgroundColor={colors.primary[400]}
                    display='flex'
                    flexDirection='column'
                    p='0.75rem'
                >
                    <Box display='flex' gap='0.5rem'>
                        <ElectricBoltIcon sx={{color: colors.greenAccent[500]}} />
                        <Typography
                            variant="h4"
                            fontWeight="bold"
                            mb='0.5rem'
                            sx={{ color: colors.grey[100] }}
                        >
                            Horas de mayor produccion
                        </Typography>
                    </Box>

                    <BarChart 
                        data={barData.horas}
                        keys={['total']}
                        indexBy={'hora'}
                    />
                </Box>

                {/* Segunda Fila */}
                <Box
                    gridColumn="span 6"
                    gridRow="span 3"
                    backgroundColor={colors.primary[400]}
                >
                    <Box
                        mt="25px"
                        p="0 30px"
                        display="flex "
                        justifyContent="space-between"
                        alignItems="center"
                    >
                        
                        <Box>
                            <Typography
                                variant="h4"
                                fontWeight="600"
                                color={colors.grey[100]}
                            >
                                Produccion mensual
                            </Typography>
                            {/* <Typography
                                variant="h3"
                                fontWeight="bold"
                                color={colors.greenAccent[500]}
                            >
                                $59,342.32
                            </Typography> */}
                        </Box> 
                       
                        <Box>
                            <IconButton>
                                <DownloadOutlinedIcon
                                sx={{ fontSize: "26px", color: colors.greenAccent[500] }}
                                />
                            </IconButton>
                        </Box>
                    </Box>
                    <Box height="250px" m="-20px 0 0 0">
                        <LineChart 
                            isDashboard={true} 
                            data={lineData}
                        />
                    </Box>
                </Box>


                <Box
                    gridColumn="span 6"
                    gridRow="span 3"
                    backgroundColor={colors.primary[400]}
                >
                    <Calendar 
                        data={calendarData}
                    />
                </Box>

                <Box
                    gridColumn="span 4"
                    gridRow="span 1"
                    backgroundColor={colors.primary[400]}
                >

                </Box>
            </Box>
        </Box>
    )
}

export default Dashboard;