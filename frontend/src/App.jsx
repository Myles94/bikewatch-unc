import { useEffect } from 'react';
import 'ol/ol.css';
import './App.css';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import BingMaps from 'ol/source/BingMaps';

function App() {
  useEffect(() => {
    new Map({
      target: 'map',
      layers: [
        new TileLayer({
          source: new BingMaps({
            key: import.meta.env.VITE_BING_MAPS_KEY,
            imagerySet: 'AerialWithLabelsOnDemand', // good for seeing UNC buildings
          }),
        }),
      ],
      view: new View({
        center: [-8800000, 4430000], // Approximate UNC-Chapel Hill location in Web Mercator
        zoom: 17,
      }),
    });
  }, []);

  return <div id="map" style={{ width: '100vw', height: '100vh' }} />;
}

export default App;
