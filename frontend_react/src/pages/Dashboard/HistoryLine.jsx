import { Box, Button, ButtonGroup, IconButton, Typography } from "@mui/material";
import LineChart from "../../Graficos/Line";

import DownloadOutlinedIcon from '@mui/icons-material/DownloadOutlined';


const HistoryLine = ({ colors, lineData, lineSpan, setLineSpan }) => {

    const spans = [
        {
            text: '1 Año',
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
            text: '1 Semana',
            key: {span: '1W', sample: '3H'}
        },
        {
            text: '1 Dia',
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
                p="1rem 1.75rem"
                display="flex "
                justifyContent="space-between"
                alignItems="center"
            >

                {/* <Box> */}
                    <Typography
                        variant="h3"
                        fontWeight="600"
                        color={colors.grey[100]}
                    >
                        Historial de produccion
                    </Typography>
                {/* </Box> */}

                <Box>
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
                    <IconButton>
                        <DownloadOutlinedIcon
                            sx={{ fontSize: "26px", color: colors.secondary[500] }}
                        />
                    </IconButton>
                </Box>
            </Box>
            
            {/* <Box 
                display='flex'
                justifyContent='flex-end'
                p='0 3rem'
            >
            </Box> */}

            <Box height="16rem">
                <LineChart
                    isDashboard={true}
                    data={lineData}
                    rotate={lineSpan.sample.endsWith('W') || lineSpan.sample.endsWith('H') || lineSpan.sample.endsWith('T')}
                />
            </Box>
        </Box>
    )
}

export default HistoryLine;