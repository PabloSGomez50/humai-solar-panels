import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import HelpOutlinedIcon from "@mui/icons-material/HelpOutlined";
import ChromeReaderModeOutlinedIcon from '@mui/icons-material/ChromeReaderModeOutlined';
import TimelineOutlinedIcon from '@mui/icons-material/TimelineOutlined';
import PieChartOutlineOutlinedIcon from "@mui/icons-material/PieChartOutlineOutlined";
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import BarChartOutlinedIcon from '@mui/icons-material/BarChartOutlined';
import CalendarMonthOutlinedIcon from '@mui/icons-material/CalendarMonthOutlined';
import TableChartIcon from '@mui/icons-material/TableChart';
import QueryStatsIcon from '@mui/icons-material/QueryStats';

export default [
    {
        name: 'Informacion del sistema',
        data: [
    //         {
    //             title: 'Grafico Torta',
    //             to: '/pie',
    //             icon: PieChartOutlineOutlinedIcon
    //         },
    //         {
    //             title: 'Grafico Linea',
    //             to: '/line',
    //             icon: TimelineOutlinedIcon
    //         },
    //         {
    //             title: 'Grafico Barras',
    //             to: '/bar',
    //             icon: BarChartOutlinedIcon
    //         },
    //         {
    //             title: 'Calendario',
    //             to: '/calendar',
    //             icon: CalendarMonthOutlinedIcon
    //         },
            {
                title: 'Tabla completa',
                to: '/table',
                icon: TableChartIcon
            },
            {
                title: 'Prediccion detallada',
                to: '/insights',
                icon: QueryStatsIcon
            },
        ]
    },
    {
        name: 'Acerca de',
        data: [
            // {
            //     title: 'Cuenta',
            //     to: '/contacts',
            //     icon: PersonOutlinedIcon
            // },
            {
                title: 'FAQ',
                to: '/faq',
                icon: HelpOutlinedIcon
            },
            // {
            //     title: 'Configuracion',
            //     to: '/settings',
            //     icon: SettingsOutlinedIcon
            // },
        
        ],
    },
]