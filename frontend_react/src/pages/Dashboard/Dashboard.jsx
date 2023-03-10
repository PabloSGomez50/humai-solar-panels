import { Box, ButtonGroup, Button, IconButton, useTheme, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import { tokens } from '../../theme';
import Header from "../../components/Header";

import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import ElectricBoltIcon from '@mui/icons-material/ElectricBolt';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import SolarPowerIcon from '@mui/icons-material/SolarPower';

import LineChart from "../../Graficos/Line";
import Calendar from "../../Graficos/Calendar";
import BarChart from "../../Graficos/Bar";
import axiosI from "../../api";
import Summary from "./Summary";
import HistoryLine from "./HistoryLine";
import DashClima from "./DashClima";

const test = []

const Dashboard = ({ userId }) => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [ year, setYear ] = useState(2012);
    const [ selectProd, setSelectProd ] = useState(true);
    const [ lineSpan, setLineSpan ] = useState({span: '1M', sample: '1D'});

    const [daily, setDaily] = useState([]);
    const [barData, setbarData] = useState({});
    const [calendarData, setCalendarData] = useState([]);
    const [lineData, setLineData] = useState([]);
    const [clima, setClima] = useState([]);

    useEffect(() => {
        
        const requestProdCalendar = async () => {
            const response = await axiosI(`calendar/${year}?user_id=${userId}`);

            console.log('EXECUTE: calendar');
            setCalendarData(response.data);
        }

        requestProdCalendar();
    }, [year, userId])

    useEffect(() => {
        
        const requestRendimiento = async () => {
            const response = await axiosI(`hist/${selectProd}/${lineSpan.span}/${lineSpan.sample}?user_id=${userId}`);

            console.log('EXECUTE: rendimiento');
            setLineData(response.data);
        }

        requestRendimiento();
    }, [lineSpan.span, selectProd, userId])

    useEffect(() => {
        
        const requestSummary = async () => {
            const response = await axiosI(`summary?user_id=${userId}`);

            console.log('EXECUTE: Horas');
            setDaily(response.data);
        }

        const requestProdHours = async () => {
            const response = await axiosI(`hours?user_id=${userId}`);

            console.log('EXECUTE: Cartas');
            setbarData(response.data);
        }
        const requestClima = async () => {
            const response = await axiosI(`clima`);

            console.log('EXECUTE: Clima');
            setClima(response.data);
        }

        requestSummary();
        requestProdHours();
        requestClima();
    }, [userId])

    return (
        <Box>
            <Box display='flex' justifyContent='space-between' alignItems='center'>
                <Header 
                    title='DASHBOARD' 
                    subtitle={`Este es el resumen del sistema ${userId}` }
                />

                <Button
                    sx={{
                        backgroundColor: colors.blueAccent[700],
                        color: colors.grey[100],
                        fontSize: "14px",
                        fontWeight: "bold",
                        padding: "0.625rem 1.25rem",
                        '&:hover': { backgroundColor: colors.blueAccent[500] }
                    }}
                >
                    <DownloadOutlinedIcon sx={{ mr: "0.625rem" }} />
                    Descargar resumen
                </Button>
            </Box>

            <Box
                display="grid"
                gridTemplateColumns="repeat(12, 1fr)"
                gridAutoRows="11rem"
                gap="1rem"
                m='0.75rem'
            >
                {/* 1ra fila 2da Columna */}
                {/* <Box
                    gridColumn='span 2'
                    gridRow='span 2'
                    backgroundColor={colors.grey[500]}
                    display='flex'
                    flexDirection='column'
                    gap='0.75rem'
                    p='0.75rem'
                >
                    <Typography variant='h4' fontWeight="bold">
                        Caracteristicas principales del sistema
                    </Typography>
                    
                    <Typography variant='h6' color={colors.secondary[400]}>
                        Capacidad instalada: 3.7 Kw
                    </Typography>
                </Box> */}

                <Summary
                    colors={colors}
                    data={daily}
                    barData={barData}
                />


                {/* 1ra fila 3er columna */}
                <Box
                    gridColumn='span 6'
                    gridRow='span 1'
                    backgroundColor={colors.grey[500]}
                    display='flex'
                    flexDirection='column'
                    p='0.75rem'
                >
                    <Box display='flex' gap='0.5rem'>
                        <SolarPowerIcon sx={{ color: colors.secondary[500] }} />
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
                        data={barData}
                        keys={['total']}
                        indexBy='hora'
                    />
                </Box>

                {/* Calendario */}
                <Box
                    gridColumn="span 6"
                    gridRow="span 1"
                    backgroundColor={colors.grey[500]}
                    // display='flex'
                    // flexDirection='column'
                >
                    <Box
                        p='0.75rem 0.75rem'
                        display='flex'
                        justifyContent='space-between'
                    >
                        
                        <Box
                            display='flex'
                            gap='0.5rem'
                        >
                            <CalendarMonthIcon sx={{ color: colors.secondary[500] }} />

                            <Typography
                                variant="h4"
                                fontWeight="bold"
                                color={colors.grey[100]}
                            >
                                Produccion historia
                            </Typography>
                        </Box>
                        
                        <ButtonGroup
                            variant="contained"
                            sx={{
                                marginRight: '0.5rem',
                                // '&:hover': {
                                //     backgroundColor: colors.primary[300]
                                // }
                            }}
                        >
                            <Button 
                                onClick={() => setYear(2012)}
                                sx={{
                                    fontWeight: 'bold',
                                    backgroundColor: year === 2012 && colors.primary[700]
                                }}
                            >
                                2012
                            </Button>
                            <Button 
                                onClick={() => setYear(2013)}
                                sx={{
                                    fontWeight: 'bold',
                                    backgroundColor: year === 2013 && colors.primary[700]
                                }}
                            >
                                2013
                            </Button>
                        </ButtonGroup>
                    </Box>
                    <Calendar
                        data={calendarData}
                    />
                </Box>

                {/* Segunda Fila */}
                {/* <Box
                    gridColumn='span 2'
                    gridRow='span 2'
                    backgroundColor={colors.grey[500]}
                    display='flex'
                    flexDirection='column'
                    p='0.75rem'
                >

                </Box> */}


                <HistoryLine
                    lineData={lineData}
                    colors={colors}
                    lineSpan={lineSpan}
                    setLineSpan={setLineSpan}
                    selectProd={selectProd}
                    setSelectProd={setSelectProd}
                />

                <DashClima 
                    clima={clima}
                    colors={colors}
                />
                <DashClima 
                    clima={clima}
                    colors={colors}
                />
            </Box>
        </Box>
    )
}

export default Dashboard;