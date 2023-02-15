import { Box, useTheme, Typography } from "@mui/material";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

import Header from "../components/Header";
import { tokens } from "../theme";


const FAQ = () => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const questions = [
        {
            id: 1,
            title: 'Pregunta importante',
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis eget.'
        },
        {
            id: 2,
            title: 'Pregunta importante',
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis eget.'
        },
        {
            id: 3,
            title: 'Pregunta importante',
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis eget.'
        },
        {
            id: 4,
            title: 'Pregunta importante',
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit leo lobortis eget.'
        }
    ]

    return (
        <Box m='1.25rem'>
            <Header title='FAQ' subtitle='Pagina de preguntas frecuentes' />
            <Box mt='2rem'>
                {questions.map(question =>     
                    <Accordion 
                        key={question.id} 
                        sx={{backgroundColor: colors.grey[900]}}
                        defaultExpanded 
                    >
                        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                            <Typography
                                color={colors.secondary[400]}
                                variant='h5'
                                >
                                {question.title}
                            </Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                            <Typography>
                                {question.text}
                            </Typography>
                        </AccordionDetails>
                    </Accordion>
                )}
            </Box>
        </Box>
    )
}

export default FAQ;