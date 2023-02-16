import { Box, Typography } from "@mui/material"
import { useEffect, useState } from "react";

const padTime = (value) => {
    if (value < 10){
        return '0' + value;
    } else {
        return value;
    }
    
}

const Clock = ({ colors }) => {
    
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
                {time.getHours()}:{padTime(time.getMinutes())}:{padTime(time.getSeconds())}
            </Typography>
        </Box>
    )
}

export default Clock;