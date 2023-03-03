import { Box, useTheme } from "@mui/material";
import { useRef } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { tokens } from "../theme";



const SidebarNew = ({ userId, setUserId }) => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const location = useLocation();
    const navigate = useNavigate();
    const gitHubRef = useRef();

    const handleSend = async () => {
        try {
            const response = await axiosI(`select_user/${modId}`);
            
            if(typeof(response.data) === 'number') {
                setMod(false);
                if (userId !== modId) {
                    if (modId === '') {
                        setUserId(1);
                    } else {
                        setUserId(modId);
                    }
                }
            }
        } catch (err){
            console.error('El usuario ' + modId + ' no esta disponible para los datos');
            setUserId(1);
        }
    }

    const handleUserId = (value) => {
        if((value > 0 && value <= 300) || value === '') {
            setModId(value);
            setMod(true);
        }
    }

    const handleBlur = () => {
        if (modId === '') {
            setModId(1);
            setMod(true);
        }
    }

    return (
        <Box
            height='100%'
            width='13rem'
            display='flex'
            flexDirection='column'
            gap='1.5rem'
            sx={{
                position: 'relative',
                top: 0,
                left: 0
            }}
        >


            e.target.value
            <a hidden ref={gitHubRef} href='https://github.com/PabloSGomez50/humai-solar-panels' target='_blank'/>
        </Box>
    )
}

export default SidebarNew;