import './App.css'
import { ColorModeContext, useMode } from './theme';
import { CssBaseline, ThemeProvider } from '@mui/material';
import { Routes, Route } from 'react-router-dom';

import TopBar from './components/TopBar';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Team from './pages/Team';
import Contacts from './pages/Contacts';
import Pie from './pages/Pie';
import Line from './pages/Line';
import FAQ from './pages/FAQ';

function App() {
  const [theme, colorMode] = useMode();

  return (
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
              <Route path='/line' element={<Line />}/>
              <Route path='/faq' element={<FAQ />}/>
              <Route path='/contacts' element={<Contacts />}/>
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  )
}

export default App
