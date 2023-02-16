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
            key: {span: '1W', sample: '6H'}
        },
        {
            text: '1 Dia',
            key: {span: '1D', sample: '30T'}
        },
    ]

    return (
        <Box
            gridColumn="span 7"
            gridRow="span 2"
            backgroundColor={colors.grey[500]}
            display='flex'
            flexDirection='column'
            gap='0.75rem'
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
                        variant="h3"
                        fontWeight="600"
                        color={colors.grey[100]}
                    >
                        Historial de produccion
                    </Typography>
                    {/* <Typography
                        variant="h4"
                        fontWeight="bold"
                        color={colors.secondary[500]}
                    >
                        Año 2013
                    </Typography> */}
                </Box>

                <Box>
                    <IconButton>
                        <DownloadOutlinedIcon
                            sx={{ fontSize: "26px", color: colors.secondary[500] }}
                        />
                    </IconButton>
                </Box>
            </Box>
            
            <Box 
                display='flex'
                justifyContent='center'
                p='0 3rem'
            >
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

            <Box height="14rem">
                <LineChart
                    isDashboard={true}
                    data={lineData}
                />
            </Box>
        </Box>
    )
}

export default HistoryLine;