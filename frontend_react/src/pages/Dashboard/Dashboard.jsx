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

const Dashboard = () => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [ year, setYear ] = useState(2012);
    const [ lineSpan, setLineSpan ] = useState('1M');

    const [daily, setDaily] = useState([]);
    const [barData, setbarData] = useState({});
    const [calendarData, setCalendarData] = useState([]);
    const [lineData, setLineData] = useState([]);

    useEffect(() => {
        
        const requestProdCalendar = async () => {
            const response = await axiosI('calendar/' + year);

            // console.log(response.data);
            setCalendarData(response.data);
        }

        requestProdCalendar();
    }, [year])

    useEffect(() => {
        
        const requestRendimiento = async () => {
            const response = await axiosI(`line/${lineSpan}`);

            // console.log(response.data);
            setLineData(response.data);
        }

        requestRendimiento();
    }, [lineSpan])

    useEffect(() => {
        const requestConsumo = async () => {
            const response = await axiosI('consumo');

            // console.log(response.data);
            setDaily(response.data);
        }

        const requestProdCards = async () => {
            const response = await axiosI('cards');

            // console.log(response.data);
            setbarData(response.data);
        }

        requestProdCards();
        requestConsumo();
        // requestProdCalendar();
        // requestRendimiento();
    }, [])

    return (
        <Box>
            <Box display='flex' justifyContent='space-between' alignItems='center'>
                <Header 
                    title='DASHBOARD' 
                    subtitle='Este es el resumen de tu sistema' 
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
                <Box
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
                </Box>

                <Summary
                    colors={colors}
                    daily={daily}
                    barData={barData}
                />


                {/* 1ra fila 3er columna */}
                <Box
                    gridColumn='span 5'
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
                        data={barData.horas}
                        keys={['total']}
                        indexBy={'hora'}
                    />
                </Box>

                {/* Calendario */}
                <Box
                    gridColumn="span 5"
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
                <Box
                    gridColumn='span 2'
                    gridRow='span 2'
                    backgroundColor={colors.grey[500]}
                    display='flex'
                    flexDirection='column'
                    p='0.75rem'
                >

                </Box>


                <HistoryLine
                    lineData={lineData}
                    colors={colors}
                    lineSpan={lineSpan}
                    setLineSpan={setLineSpan}
                />

                <Box
                    gridColumn='span 3'
                    gridRow='span 2'
                    backgroundColor={colors.grey[500]}
                    display='flex'
                    flexDirection='column'
                    p='0.75rem'
                >

                </Box>
                
            </Box>
        </Box>
    )
}

export default Dashboard;