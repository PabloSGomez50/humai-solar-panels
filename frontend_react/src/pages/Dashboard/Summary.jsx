import { Box, Typography } from "@mui/material";


import ElectricBoltIcon from '@mui/icons-material/ElectricBolt';
import SolarPowerIcon from '@mui/icons-material/SolarPower';
import SummaryLine from "./SummaryLine";

const Summary = ({ colors, daily }) => {

    const arr = [1,2,3,4]
    console.log(daily)

    return (
        <Box
            gridColumn='span 5'
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
                        <Box>
                            <Typography variant="h4">
                                Total: 
                            </Typography>
                            <Typography variant="h4">
                                {daily.total} Kw
                            </Typography>
                        </Box>

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
        </Box>
    )
}

export default Summary;