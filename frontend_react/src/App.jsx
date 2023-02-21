import './App.css'
import { ColorModeContext, useMode } from './theme';
import { Box, CssBaseline, ThemeProvider } from '@mui/material';
import { Routes, Route } from 'react-router-dom';
import { ProSidebarProvider } from 'react-pro-sidebar';

import TopBar from './components/TopBar';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard/Dashboard';
import Table from './pages/Table';
import Insights from './pages/Insights';
import Config from './pages/Config';
import FAQ from './pages/FAQ';

import { tokens } from './theme';
import { useEffect } from 'react';

function App() {
  const [theme, colorMode] = useMode();
  const colors = tokens(theme.palette.mode);

  useEffect(() => {
    document.body.style.backgroundColor = colors.grey[800];
  }, [])

  return (
    <ProSidebarProvider>
      <ColorModeContext.Provider value={colorMode}>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <div className="app">
            <Sidebar />
            <main className='content'>
              <TopBar />
                <Box 
                  height='100%' 
                  // backgroundColor={colors.primary[700]} 
                  backgroundColor={colors.grey[800]} 
                  p='1.25rem 2rem'
                >
                  <Routes>
                    <Route path='/' element={<Dashboard />}/>
                    <Route path='/table' element={<Table />}/>
                    <Route path='/faq' element={<FAQ />}/>
                    <Route path='/insights' element={<Insights />}/>
                    <Route path='/settings' element={<Config />}/>
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
