import { Box, Typography } from "@mui/material"
import { useEffect, useState } from "react";



const Clock = ({ colors }) => {

    console.log('Re render Clock')

    const [ time, setTime] = useState(new Date());

    useEffect(() => {
        const interval_id = setInterval(() => setTime(new Date()), 1000);

        return () => {
            clearInterval(interval_id);
        }
    }, [])

    return (
        <Box
            backgroundColor={colors.primary[600]}
            borderRadius='0.75rem'
        >
            <Typography
                fontSize='24px'
                p='0 1.75rem'
            >
                {time.getHours()}:{time.getMinutes()}:{time.getSeconds()}
            </Typography>
        </Box>
    )
}

export default Clock;