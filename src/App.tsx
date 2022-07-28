import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import { Counter } from './features/counter/Counter';
import './App.css';
import {data} from "./data";

function App() {
  const [dungeon, setDungeon] = useState(data[0].id)
 const [lang, setLang] = useState("de")

const renderBossSelect=(did:number)=>{
  return  data.find(d=>d.id===dungeon)?.bosses.map(boss=>{


    return<div><h2>{boss.name}</h2>
    <div style={{display:"flex",flex:1,alignContent:"center",justifyContent:"center"}}>
      <div>
        <h3>NHC</h3>
{renderLoot(dungeon,boss.name)}
      </div>
      <div>
        <h3>HC</h3>
{renderLootHC(dungeon,boss.name)}
      </div>
     </div>
    </div>
  })
}

const renderLoot=(did:number,bossName:string)=>{
  console.log("render loot",did,bossName);
  
  return data.find(d=>d.id===did)?.bosses.find(b=>b.name===bossName)?.lootNHC.map(loot=><div><a href="#"  data-wowhead={"item="+loot.id+"&domain="+lang}>{loot.name}</a></div>
  ) 
}
const renderLootHC=(did:number,bossName:string)=>{
  console.log("render loot",did,bossName);
  
  return data.find(d=>d.id===did)?.bosses.find(b=>b.name===bossName)?.lootHC.map(loot=><div><a href="#"  data-wowhead={"item="+loot.id+"&domain="+lang}>{loot.name}</a></div>
  ) 
}
  return (
    <div className="App">
     <select  onChange={e=>setDungeon(parseInt(e.target.value))}>
      {data.map(d=>{return<option value={d.id}>{d.name}</option>})}
     </select>
     <select onChange={e=>setLang(e.target.value)}>
      <option value="de">DE</option>
      <option value={"den"}>EN</option>
     </select>
    {renderBossSelect(dungeon)}
     
    </div>
  );
}

export default App;
