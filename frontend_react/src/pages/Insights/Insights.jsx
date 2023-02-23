import { Box, Typography, useTheme } from "@mui/material";
import { useEffect, useState } from "react";

import axiosI from "../../api";
import { tokens } from "../../theme";
import Header from "../../components/Header";

import InsightsGraph from "./InsightsGraph";
import { DataGrid } from "@mui/x-data-grid";


const columns = [
    { field: "id", headerName: "ID" },
    {
        field: "Fecha",
        //   headerName: "Name",
        type: 'date',
        //   width: '5rem',
        cellClassName: "name-column--cell",
    },
    {
        field: "Produccion",
        headerName: "Produccion (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        flex: 1,
    },
    {
        field: "GC",
        headerName: "Consumo general (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        
        flex: 1,
    },
    {
        field: "CL",
        headerName: "Consumo controlado (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        
        flex: 1,
    },
    {
        field: "Diferencia",
        headerName: "Diferencia (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        flex: 1,
        renderCell: (d) => {
            const value = d.formattedValue;
            const positive = value >= 0;
            // console.log(d);
            
            return (
            <Box 
                color={positive ? '#9CFF2E': '#F00'}
                fontWeight='bold'
            >
                {positive && '+'} {value} Kw
            </Box>
        )}
    },
    {
        field: "Total",
        headerName: "Consumo Total (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        
        flex: 1,
    },
];


const Insights = ({ userId }) => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [ prod, setProd ] = useState(true);
    const [ data, setData ] = useState([]);
    const [ predict, setPredict ] = useState([]);


    useEffect(() => {
        const requestGrafico = async () => {
            const lineSpan = {
                span: '2D',
                sample: '1H'
            }
            const response = await axiosI(`hist/${prod}/${lineSpan.span}/${lineSpan.sample}?user_id=${userId}`)

            console.log(response.data);
            setData(response.data);
        }
        const requestPredict = async () => {
            const response = await axiosI(`prediccion/?user_id=${userId}`)

            console.log(response.data);
            setPredict(response.data);
        }

        requestGrafico();
        prod && requestPredict();
    }, [prod, userId])

    const filterData = () => {
        // return data.filter(item => )
        console.log('Test');
        console.log(data);
        console.log(predict);
        predict && predict[0] && predict[0].data && console.log(predict[0].data);
        
        console.log([...data, ...predict])
        return [...data, ...predict];
    }

    return (
        <Box>
            <Header 
                title='Prediccion de rendimiento'
                subtitle='Seccion enfocada a los datos de prediccion de la red ML'
            />
            
            <Box
                display='grid'
                margin='1rem 0'
                width='97%'
                p='1.5rem'
                gap='1rem'
                backgroundColor={colors.grey[500]}
            >
            {/* 
                <Box display='flex' alignItems='center' gap='0.75rem'>
                    
                    <Box 
                        display='flex' 
                        alignItems='center' 
                        justifyContent='space-around' 
                        gap='0.75rem'
                    >
                        <Typography
                            onClick={() => setProd(true)}
                            fontSize='1.75rem'
                            sx={{
                                opacity: prod ? '1' : '0.6'
                                
                            }}
                        >
                            Produccion
                        </Typography>
                        <Typography
                            fontSize='1.75rem'
                        >
                            /
                        </Typography>
                        <Typography
                            pt='2px'
                            onClick={() => setProd(false)}
                            fontSize='1.75rem'
                            sx={{
                                opacity: prod ? '0.6' : '1'
                            }}
                        >
                            Consumo
                        </Typography>
                    </Box>
                </Box> 
                */}

                <Box
                    // backgroundColor='#f00'
                    height='40vh'
                    display='flex' 
                    alignItems='center' 
                    justifyContent='center'
                >
                    {data && data.length > 0 ?
                        <InsightsGraph
                            data={filterData()}
                            colors={colors}
                        />
                        :
                        <Typography fontSize='2rem'>
                            No hay datos disponibles
                        </Typography>
                    }
                </Box>
            
            </Box>

            {/* {predict && predict[0] && 
            <Box
                m="16px 0 0 0"
                height="30vh"
                sx={{
                    "& .MuiDataGrid-root": {
                        border: "none",
                    },
                    "& .MuiDataGrid-cell": {
                        borderBottom: "none",
                        backgroundColor: colors.grey[500]
                    },
                    "& .name-column--cell": {
                        color: colors.secondary[300]
                    },
                    "& .MuiDataGrid-columnHeaders": {
                        backgroundColor: colors.blueAccent[700],
                        borderBottom: "none",
                    },
                    "& .MuiDataGrid-virtualScroller": {
                        backgroundColor: colors.grey[900]
                    },
                    "& .MuiDataGrid-footerContainer": {
                        borderTop: "none",
                        backgroundColor: colors.blueAccent[700],
                    },
                    "& .MuiCheckbox-root": {
                        color: `${colors.secondary[200]} !important`,
                    },
                }}
            >
                <DataGrid
                    checkboxSelection 
                    rows={predict[0].data} 
                    columns={columns} 
                />
            </Box>
        } */}
        </Box>
    )
}

export default Insights;