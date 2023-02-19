import { Box, Typography } from "@mui/material";


import ElectricBoltIcon from '@mui/icons-material/ElectricBolt';
import SolarPowerIcon from '@mui/icons-material/SolarPower';
import SummaryLine from "./SummaryLine";

const Summary = ({ colors, data }) => {

    const order = ['consumo_dia', 'prod_dia', 'consumo_week', 'prod_week']
    const textos = {
        'consumo_dia': 'Consumo semanal', 
        'prod_dia': 'Produccion semanal', 
        'consumo_week': 'Consumo Mensual', 
        'prod_week': 'Produccion Mensual'
    }
    
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
            {order.map(item => 
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
                            mb='0.25rem'
                            sx={{ color: colors.grey[100] }}
                        >
                            {textos[item]}
                        </Typography>
                        <ElectricBoltIcon sx={{ color: colors.secondary[500] }} />
                    </Box>


                    {data[item] && 
                    <Box
                    height='100%'
                    display='flex'
                    alignItems='center'
                    justifyContent='space-around'
                    >
                        <Box>
                            <Typography variant="h4">
                                {item.endsWith('dia') ? 'Total' : 'Actual'}
                            </Typography>
                            <Typography variant="h4">
                                {data[item].total} Kw
                            </Typography>
                        </Box>

                        {data[item].dias &&
                            <Box width='65%' height='6.5rem'>
                                <SummaryLine
                                    info={data[item].dias}
                                    colors={colors}
                                    rotate={item.endsWith('dia')}
                                    />
                            </Box>
                        }
                    </Box>
                    }
                </Box>
            )}
        </Box>
    )
}

export default Summary;