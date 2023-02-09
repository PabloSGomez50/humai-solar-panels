import { useTheme } from "@mui/material";
import { tokens } from "../../theme";
import { ResponsiveCalendar } from '@nivo/calendar';
import { mockCalendar } from "../../fake_data/data";

const Calendar = ({data}) => {

    let from = "2015-09-02";
    let to = "2016-11-26";


    if (data && data.length > 0) {
        const len = data.length;
        from = data[0].day;
        to = data[len - 1].day;
        
    } else {
        data = mockCalendar;
    }

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const colorSchema = {
        textColor: '#FFF',
        fontSize: '16px',
        tooltip: {
            container: {
                color: colors.grey[400]
            }
        }
    }

    return (
        <ResponsiveCalendar
            data={data}
            theme={colorSchema}
            from={from}
            to={to}
            colors={[ 
                colors.blueAccent[200], 
                colors.blueAccent[400], 
                colors.blueAccent[500], 
                colors.blueAccent[700]
            ]}
            margin={{ top: 40, right: 40, bottom: 40, left: 40 }}
            yearSpacing={40}
            monthBorderColor={colors.grey[500]}
            dayBorderColor='#e3e3e3'
            emptyColor='transparent'
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