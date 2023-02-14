import './App.css'
import { ColorModeContext, useMode } from './theme';
import { Box, CssBaseline, ThemeProvider } from '@mui/material';
import { Routes, Route } from 'react-router-dom';
import { ProSidebarProvider } from 'react-pro-sidebar';

import TopBar from './components/TopBar';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Table from './pages/Table';
import Contacts from './pages/Contacts';
import Pie from './Graficos/Pie';
import Line from './Graficos/Line';
import Bar from './Graficos/Bar';
import Calendar from './Graficos/Calendar';
import FAQ from './pages/FAQ';

import { tokens } from './theme';

function App() {
  const [theme, colorMode] = useMode();
  const colors = tokens(theme.palette.mode);


  return (
    <ProSidebarProvider>
      <ColorModeContext.Provider value={colorMode}>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <div className="app">
            <Sidebar />
            <main className='content'>
              <TopBar />
                <Box height='100%' backgroundColor={colors.primary[900]}>
                  <Routes>
                    <Route path='/' element={<Dashboard />}/>
                    <Route path='/table' element={<Table />}/>
                    {/* 
                    <Route path='/pie' element={<Pie />}/>
                    <Route path='/bar' element={<Bar />}/>
                    <Route path='/line' element={<Line />}/>
                    <Route path='/calendar' element={<Calendar />}/>
                    */}

                    <Route path='/faq' element={<FAQ />}/>
                    <Route path='/contacts' element={<Contacts />}/>
                    <Route path='/settings' element={<Contacts />}/>
                  </Routes>
                </Box>
            </main>
          </div>
        </ThemeProvider>
      </ColorModeContext.Provider>
    </ProSidebarProvider>
  )
}

export default App
