import { useEffect } from 'react'
import 'ol/ol.css'
import './App.css'
import Map from 'ol/Map'
import View from 'ol/View'
import TileLayer from 'ol/layer/Tile'
import XYZ from 'ol/source/XYZ'
import { fromLonLat } from 'ol/proj'

function App() {
  useEffect(() => {
    new Map({
      target: 'map',
      layers: [
        new TileLayer({
          source: new XYZ({
            url: `https://api.maptiler.com/maps/satellite/{z}/{x}/{y}.jpg?key=${import.meta.env.VITE_MAPTILER_KEY}`,
            tileSize: 512,
            crossOrigin: 'anonymous',
          }),
        }),
      ],
      view: new View({
        center: fromLonLat([-79.0469, 35.9101]),
        zoom: 17,
      }),
    })
  }, [])

  return <div id="map" style={{ width: '100vw', height: '100vh' }} />
}

export default App

