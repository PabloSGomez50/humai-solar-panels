import { Box, Typography } from "@mui/material";


import ElectricBoltIcon from '@mui/icons-material/ElectricBolt';
import SolarPowerIcon from '@mui/icons-material/SolarPower';
import SummaryLine from "./SummaryLine";

const Summary = ({ colors, daily }) => {

    const arr = [1,2,3,4]
    console.log(daily)

    return (
        <Box
            gridColumn='span 6'
            gridRow='span 2'

            // p='0.25rem'
            // backgroundColor={colors.grey[500]}
            display='grid'
            gridTemplateColumns='1fr 1fr'
            gridTemplateRows='1fr 1fr'
            gap='0.75rem'
        >
            {arr.map(item => 
                <Box 
                    key={item}
                    p='1rem'
                    display='flex' 
                    flexDirection='column' 
                    backgroundColor={colors.grey[500]}
                >
                    <Box display='flex' gap='0.5rem' justifyContent='space-between'>
                        <Typography
                            variant="h4"
                            fontWeight="bold"
                            mb='0.75rem'
                            sx={{ color: colors.grey[100] }}
                        >
                            Consumo semanal
                        </Typography>
                        <ElectricBoltIcon sx={{ color: colors.secondary[500] }} />
                    </Box>

                    <Box
                        height='100%'
                        display='flex'
                        alignItems='center'
                        justifyContent='space-around'
                    >
                        <Typography variant="h4">
                            Total: {daily.total} Kw
                        </Typography>

                        {daily.dias &&
                            <Box width='65%' height='6.5rem'>
                                <SummaryLine
                                    info={daily.dias}
                                    colors={colors}
                                />
                            </Box>
                        }
                    </Box>
                </Box>
            )}

            {/* <Typography variant="h4" backgroundColor={colors.grey[400]}>
                El total del dia es {daily.total} Kw
            </Typography> */}

            {/* <Box
                display='flex'
                height='90%'
                flexDirection='column'
                gap='0.5rem'
                flexWrap='wrap'
            >
                {daily.dias && daily.dias.map(item =>
                    <Box
                        key={item.day}
                        display='flex'
                        justifyContent='space-between'
                        p='0 0.5rem'
                    >
                        <Typography sx={{ color: colors.grey[100] }}>
                            {item.day}
                        </Typography>

                        <Typography sx={{ color: colors.primary[100] }}>
                            {item.value} Kw
                        </Typography>
                    </Box>
                )}
            </Box> */}

        </Box>
    )
}

export default Summary;