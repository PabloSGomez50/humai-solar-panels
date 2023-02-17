import { ResponsiveLine } from "@nivo/line";



const SummaryLine = ({ info, colors, rotate }) => {
    
    const data = [
        {id: 'Consumo', color: '#e8c1a0', data: info}
    ]

    return (
        <ResponsiveLine
            data={data}
            margin={{ top: 10, right: 15, bottom: 30, left: 15 }}
            xScale={{ type: 'point' }}
            yScale={{
                type: 'linear',
                min: '0',
                max: 'auto',
                stacked: false,
                reverse: false
            }}
            yFormat=" >-.2f"
            curve="monotoneX"
            colors={{ scheme: 'category10' }} // paired | category10
            axisTop={null}
            axisRight={null}
            axisBottom={
                {
                orient: 'bottom',
                tickSize: 5,
                tickPadding: 5,
                tickRotation: rotate ? -45 : 0,
                // legend: 'transportation',
                // legendOffset: 36,
                // legendPosition: 'middle'
                }
            }
            axisLeft={null
                // {
                // orient: 'left',
                // tickSize: 5,
                // tickPadding: 5,
                // tickRotation: 1,
                // legend: 'count',
                // legendOffset: -40,
                // legendPosition: 'middle'
                // }
            }
            enableGridY={false}
            pointColor={{ theme: 'background' }}
            pointBorderWidth={2}
            pointBorderColor={{ from: 'serieColor' }}
            pointLabelYOffset={-12}
            enableArea={true}
            areaBaselineValue={0}
            areaOpacity={0.3}
            useMesh={true}

            theme={{
                axis: {
                    ticks: {
                        line: {
                            stroke: colors.grey[400]
                        },
                        text: {
                            fill: colors.grey[100]
                        }
                    }
                },
                tooltip: {
                    container: {
                        color: colors.grey[400]
                    }
                }
            }}

            // legends={[
            //     {
            //         anchor: 'bottom-right',
            //         direction: 'column',
            //         justify: false,
            //         translateX: 100,
            //         translateY: 0,
            //         itemsSpacing: 0,
            //         itemDirection: 'left-to-right',
            //         itemWidth: 80,
            //         itemHeight: 20,
            //         itemOpacity: 0.75,
            //         symbolSize: 12,
            //         symbolShape: 'circle',
            //         symbolBorderColor: 'rgba(0, 0, 0, .5)',
            //         effects: [
            //             {
            //                 on: 'hover',
            //                 style: {
            //                     itemBackground: 'rgba(0, 0, 0, .03)',
            //                     itemOpacity: 1
            //                 }
            //             }
            //         ]
            //     }
            // ]}
        />
    )
}

export default SummaryLine;