


const DashContent = () => {

    return (

        <Box
            display="grid"
            gridTemplateColumns="repeat(12, 1fr)"
            gridAutoRows="120px"
            gap="1.25rem"
            m='1rem'
        >
            {/* 1ra fila 1er columna */}
            <Box
                gridColumn='span 4'
                gridRow='span 2'
                backgroundColor={colors.grey[500]}
                display='flex'
                flexDirection='column'
                p='0.75rem'
            >
                <Box display='flex' gap='0.5rem'>
                    <ElectricBoltIcon sx={{ color: colors.secondary[500] }} />
                    <Typography
                        variant="h4"
                        fontWeight="bold"
                        mb='0.75rem'
                        sx={{ color: colors.grey[100] }}
                    >
                        Consumo semanal
                    </Typography>
                </Box>

                <Typography variant="h4">
                    El total del dia es {daily.total} Kw
                </Typography>

                <Box
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
                </Box>

            </Box>

            {/* 1ra fila 2er columna */}
            <Box
                gridColumn='span 4'
                gridRow='span 2'
                backgroundColor={colors.grey[500]}
                display='flex'
                flexDirection='column'
                p='0.75rem'
            >
                <Box display='flex' gap='0.5rem'>
                    <ElectricBoltIcon sx={{ color: colors.secondary[500] }} />
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

            {/* Segunda Fila */}
            <Box
                gridColumn="span 6"
                gridRow="span 3"
                backgroundColor={colors.grey[500]}
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
                            Produccion mensual
                        </Typography>
                        <Typography
                            variant="h4"
                            fontWeight="bold"
                            color={colors.secondary[500]}
                        >
                            Año 2013
                        </Typography>
                    </Box>

                    <Box>
                        <IconButton>
                            <DownloadOutlinedIcon
                                sx={{ fontSize: "26px", color: colors.secondary[500] }}
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
                backgroundColor={colors.grey[500]}
            >
                <Box
                    pl='1rem'
                    pt='0.5rem'
                >
                    <Typography
                        variant="h3"
                        fontWeight="600"
                        color={colors.grey[100]}
                    >
                        Produccion historia
                    </Typography>
                    <Typography
                        variant="h4"
                        fontWeight="bold"
                        color={colors.secondary[500]}
                    >
                        Por dia
                    </Typography>
                </Box>
                <Calendar
                    data={calendarData}
                />
            </Box>

            {/* <Box
            gridColumn="span 4"
            gridRow="span 1"
            backgroundColor={colors.grey[500]}
        >

        </Box> */}
        </Box>
    )
}

export default DashContent;