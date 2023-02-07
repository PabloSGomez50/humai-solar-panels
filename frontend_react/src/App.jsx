import './App.css'
import { ColorModeContext, useMode } from './theme';
import { CssBaseline, ThemeProvider } from '@mui/material';
import { Routes, Route } from 'react-router-dom';
import { ProSidebarProvider } from 'react-pro-sidebar';

import TopBar from './components/TopBar';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Team from './pages/Team';
import Contacts from './pages/Contacts';
import Pie from './pages/Graficos/Pie';
import Line from './pages/Graficos/Line';
import Bar from './pages/Graficos/Bar';
import Calendar from './pages/Graficos/Calendar';
import FAQ from './pages/FAQ';

function App() {
  const [theme, colorMode] = useMode();

  return (
    <ProSidebarProvider>
      <ColorModeContext.Provider value={colorMode}>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <div className="app">
            <Sidebar />
            <main className='content'>
              <TopBar /> 
              <Routes>
                <Route path='/' element={<Dashboard />}/>
                <Route path='/team' element={<Team />}/>
                <Route path='/pie' element={<Pie />}/>
                <Route path='/bar' element={<Bar />}/>
                <Route path='/line' element={<Line />}/>
                <Route path='/calendar' element={<Calendar />}/>


                <Route path='/faq' element={<FAQ />}/>
                <Route path='/contacts' element={<Contacts />}/>
                <Route path='/settings' element={<Contacts />}/>
              </Routes>
            </main>
          </div>
        </ThemeProvider>
      </ColorModeContext.Provider>
    </ProSidebarProvider>
  )
}

export default App
