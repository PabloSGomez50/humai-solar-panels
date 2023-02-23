import { Box, Button, ButtonGroup, IconButton, Typography } from "@mui/material";
import LineChart from "../../Graficos/Line";

import LoopIcon from '@mui/icons-material/Loop';
import TimelineIcon from '@mui/icons-material/Timeline';
import { useEffect, useState } from "react";


const HistoryLine = ({ colors, lineData, lineSpan, setLineSpan, selectProd, setSelectProd }) => {

    const [ticks, setTicks] = useState(undefined);

    useEffect(() => {
        const arr = [];
        if (lineSpan.span === '1W' && lineData.length > 0) {
            for (const value of lineData[0].data) {
                
                const time = value.x.split(' ')[1];

                if (arr.every(item => item.split(' ')[1] !== time)) {
                    arr.push(value.x);
                }
            }

            setTicks(arr);
        }

    }, [lineData]);

    const spans = [
        {
            // text: '1 Año',
            text: '12 Meses',
            key: {span: '1Y', sample: '1W'}
        },
        {
            text: '3 Meses',
            key: {span: '3M', sample: '1D'}
        },
        {
            text: '1 Mes',
            key: {span: '1M', sample: '1D'}
        },
        {
            // text: '1 Semana',
            text: '7 Dias',
            key: {span: '1W', sample: '2H'}
        },
        {
            // text: '1 Dia',
            text: '24 Hs',
            key: {span: '1D', sample: '30T'}
        },
    ]

    return (
        <Box
            gridColumn="span 8"
            gridRow="span 2"
            backgroundColor={colors.grey[500]}
            display='flex'
            flexDirection='column'
            gap='0.75rem'
        >
            <Box
                p="1rem 1.75rem 0.75rem"
                display="flex"
                justifyContent="space-between"
                alignItems="center"
            >

                <Box display='flex' alignItems='center' gap='0.75rem'>
                    <TimelineIcon
                        sx={{ fontSize: "26px", color: colors.secondary[500] }}
                    />
                    <Typography
                        variant="h3"
                        fontWeight="600"
                        color={colors.grey[100]}
                    >
                        Historial de {selectProd ? 'produccion' : 'consumo'}
                    </Typography>
                    
                    {lineSpan.span === '3M' &&
                        <IconButton>
                            <LoopIcon
                                onClick={() => setSelectProd(prev => !prev)}
                                sx={{ fontSize: "26px", color: colors.secondary[500] }}
                            />
                        </IconButton>
                    }
                </Box>

                <Box display='flex' alignItems='center' gap='0.75rem'>
                    <ButtonGroup
                        variant="contained"
                    >
                        {spans.map(item =>     
                            <Button
                                key={item.key.span}
                                onClick={() => setLineSpan(item.key)}
                                sx={{
                                    backgroundColor: lineSpan.span === item.key.span && colors.primary[700]
                                }}
                            >
                                {item.text}
                            </Button>
                        )}

                    </ButtonGroup>
                </Box>
            </Box>
            
            <Box height="16rem">
                <LineChart
                    data={lineData}
                    rotate={lineSpan.sample.endsWith('W') || lineSpan.sample.endsWith('T')}
                    tickValues={lineSpan.span === '1W' ? ticks : undefined}
                />
            </Box>
        </Box>
    )
}

export default HistoryLine;