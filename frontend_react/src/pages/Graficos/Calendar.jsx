import { useTheme } from "@mui/material";
import { tokens } from "../../theme";
import { ResponsiveCalendar } from '@nivo/calendar';

const Calendar = () => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const data = [
        {
            "value": 128,
            "day": "2016-11-26"
        },
        {
            "value": 185,
            "day": "2017-08-03"
        },
        {
            "value": 257,
            "day": "2017-03-28"
        },
        {
            "value": 12,
            "day": "2015-10-24"
        },
        {
            "value": 366,
            "day": "2015-09-02"
        },
    ]

    const colorSchema = {
        textColor: '#FFF'
    }

    return (
        <ResponsiveCalendar
            data={data}
            theme={colorSchema}
            from="2015-03-01"
            to="2016-07-12"
            emptyColor='#a3a3a3'
            colors={[ colors.redAccent[500], '#97e3d5', '#e8c1a0', '#f47560']}
            margin={{ top: 40, right: 40, bottom: 40, left: 40 }}
            yearSpacing={40}
            monthBorderColor='#e3e3e3'
            dayBorderColor='#e3e3e3'
            dayBorderWidth={2}
            legends={[
                {
                    anchor: 'bottom-right',
                    direction: 'row',
                    translateY: 36,
                    itemCount: 4,
                    itemWidth: 42,
                    itemHeight: 36,
                    itemsSpacing: 14,
                    itemDirection: 'right-to-left'
                }
            ]}
        />
    )
}

export default Calendar;