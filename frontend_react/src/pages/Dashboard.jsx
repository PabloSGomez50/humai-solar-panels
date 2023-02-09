import { Box, Button, IconButton, useTheme, Typography } from "@mui/material";
import { tokens } from '../theme';
import Header from "../components/Header";
import axios from 'axios';

import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import EmailIcon from "@mui/icons-material/Email";
import StatBox from "../components/StatBox";
import LineChart from "./Graficos/Line";
import Calendar from "./Graficos/Calendar";
import { useEffect, useState } from "react";

const Dashboard = () => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [daily, setDaily] = useState([]);

    const stats = [
        // {
        //     title: 'Total de produccion',
        //     subtitle: 'En los ultimos 7 dias',
        //     progress: 0.75,
        //     increase: 14,
        //     icon:
        //     <EmailIcon
        //         sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
        //     />
        // },
        {
            title: 'Promedio diario',
            subtitle: 'En los ultimos 7 dias',
            progress: 0.75,
            increase: 14,
            icon:
            <EmailIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
            />
        },
        {
            title: 'Hora de mayor produccion',
            subtitle: 'En los ultimos 7 dias',
            progress: 0.33,
            increase: 14,
            icon:
            <EmailIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
            />
        },
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
        const requestData = async () => {
            const response = await axios(
                'http://127.0.0.1:8000/data'
            )

            console.log(response.data);
            const total = response.data.reduce(
                (prev, current) => Math.round((prev + current.value) * 100) / 100
                , 0)
            const arr = [...response.data, {day: 'Total', value: total}]
            setDaily(arr);
        }

        requestData()
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
                gridAutoRows="140px"
                gap="1.25rem"
                m='1rem'
            >
                <Box
                    gridColumn='span 3'
                    backgroundColor={colors.primary[400]}
                    display='flex'
                    flexDirection='column'
                    p='0.75rem'
                >
                    <Typography
                        variant="h4"
                        fontWeight="bold"
                        sx={{ color: colors.grey[100] }}
                    >
                        Consumo Total
                    </Typography>

                    <Box
                        display='flex'
                        height='90%'
                        flexDirection='column'
                        gap='0.25rem'
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



                {stats.map(stat =>     
                    <Box
                        key={stat.title}
                        gridColumn='span 3'
                        backgroundColor={colors.primary[400]}
                        display='flex'
                        alignItems='center'
                        justifyContent='center'
                    >

                        <StatBox
                            title={stat.title}
                            subtitle={stat.subtitle}
                            progress={stat.progress}
                            increase={`+${stat.increase}%`}
                            icon={stat.icon}
                        />
                    </Box>
                )}

                <Box
                    gridColumn="span 8"
                    gridRow="span 2"
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
                                variant="h5"
                                fontWeight="600"
                                color={colors.grey[100]}
                            >
                                Revenue Generated
                            </Typography>
                            <Typography
                                variant="h3"
                                fontWeight="bold"
                                color={colors.greenAccent[500]}
                            >
                                $59,342.32
                            </Typography>
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
                        <LineChart isDashboard={true} />
                    </Box>
                </Box>


                <Box
                    gridColumn="span 4"
                    gridRow="span 2"
                    backgroundColor={colors.primary[400]}
                >
                    <Calendar />
                </Box>
            </Box>
        </Box>
    )
}

export default Dashboard;