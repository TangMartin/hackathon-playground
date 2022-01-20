import React, { useState, useEffect } from 'react';

import { Button, Typography, Layout, List, Row, Card} from 'antd';
import 'antd/dist/antd.css';


import like from './assets/lovewhite.png'
import liked from './assets/heart.png'

import './App.css';

import axios from 'axios';

const { Content } = Layout;

function App() {

  const data = [
    {
        title: 'Title 1',
    },
    {
        title: 'Title 2',
    },
    {
        title: 'Title 3',
    },
    {
        title: 'Title 4',
    },
    {
        title: 'Title 1',
    },
    {
        title: 'Title 2',
    },
    {
        title: 'Title 3',
    },
    {
        title: 'Title 4',
    },
    {
        title: 'Title 1',
    },
    {
        title: 'Title 2',
    },
    {
        title: 'Title 3',
    },
    {
        title: 'Title 4',
    },
    {
        title: 'Title 1',
    },
    {
        title: 'Title 2',
    },
    {
        title: 'Title 3',
    },
    {
        title: 'Title 4',
    },
    {
        title: 'Title 1',
    },
    {
        title: 'Title 2',
    },
    {
        title: 'Title 3',
    },
    {
        title: 'Title 4',
    },
    {
        title: 'Title 1',
    },
    {
        title: 'Title 2',
    },
    {
        title: 'Title 3',
    },
    {
        title: 'Title 4',
    },
    {
        title: 'Title 3',
    },
    {
        title: 'Title 4',
    },
    {
        title: 'Title 1',
    },
    {
        title: 'Title 2',
    },
    {
        title: 'Title 3',
    },
    {
        title: 'Title 4',
    }
];
  const [userID, SetUserID] = useState('Martin Tang')
  const [PhotoData, SetPhotoData] = useState([])

  useEffect(() => {
    try {
      var configUser = {
          method: 'get',
          url: `https://api.nasa.gov/planetary/apod?start_date=${getCurrentDate()[1]}&end_date=${getCurrentDate()[0]}&api_key=EXKq34qFD0W8ewQwPUN1v2FTaBllzjnjvSLoSjF7`,
          headers: {
              'Content-Type': 'application/json'
          },
          data: {}
      };
      axios(configUser).then((userRes) => {
          SetPhotoData(userRes.data);

          for (var i in userRes.data)
          {
            userRes.data[i]['liked'] = false;
          }
          console.log(userRes.data)
      })
      
  } catch (e) {
      console.log(e);
  }

  }, [userID])



  const getCurrentDate=()=>{

    var date = new Date().getDate();
    var month = new Date().getMonth() + 1;
    var year = new Date().getFullYear();

    const today = year + '-' + '0'+ month + '-' + date;
    const firstdayofthemonth = year + '-' + '0'+ month + '-' + '01';

    return [today, firstdayofthemonth]
  }

  return (
    <Layout style={{
      textAlign: 'center',
      maxWidth: "100vw",
      backgroundColor: 'white',
    }}>
      <Layout>
        <Content style={{
            width: '100%',
            paddingTop: "2%",
            paddingLeft: '5%',
            paddingRight: '5%',
            backgroundColor: 'white',
            textAlign: 'center',         
        }}>
          <div>
            <text style={{
              fontSize: 60,
              fontWeight: 600,
            }}>
              NASA Photo of the Day for the Month
            </text>
            <Row type="flex" style={{
              justifyContent: 'center',
              paddingBottom: '3%'
            }}>
              <text style={{
                fontSize: 30,
                fontWeight: 600,
              }}>
                By Martin Tang 
              </text>
            </Row>
          </div>
          <div style={{
            backgroundColor: '#FCEF91',
            borderRadius:  50,
          }}>

            <List
              grid={{ gutter: 18, column: 3 }}
              dataSource={PhotoData}
              style={{
                padding: '2%'
              }}
              renderItem={ (item, index) => (
                <List.Item>
                  <div style={{
                        padding: 10,
                        height: 400,
                        width: 480,
                        borderTopRightRadius: '20px',
                        borderTopLeftRadius: '20px',
                        position: 'relative',
                        backgroundColor: 'white',
                    }}>
                      
                        <img src={item.url} style={{
                            width: '100%',
                            height: '100%',
                            borderRadius: '20px',

                            objectFit: 'cover',
                        }}></img>
                        <img src={PhotoData[index].liked ? liked : like} style={{
                          position: 'absolute',
                          top: 30,
                          right: 30,
                          height: 35,
                          width: 35,
                          color: 'white',}}
                          onClick={() => {
                            console.log(PhotoData[index].liked)
                            if(PhotoData[index].liked === true)
                            {
                              alert(`${item.title} is UNLIKED`)
                              PhotoData[index].liked = false; 
                              
                            }
                            else
                            {
                              PhotoData[index].liked = true; 
                              alert(`${item.title} is LIKED`)
                            }
                          
                          }}
                          >
                        </img>
                    </div>
                    <div style={{
                        padding: 5,
                        height: 100,
                        width: 480,
                        borderBottomRightRadius: '20px',
                        borderBottomLeftRadius: '20px',
                        position: 'relative',
                        backgroundColor: 'white',
                    }}>
                    <div style={{
                      paddingLeft: 10,
                      marginBottom: 10,
                    }}>
                      
                      <Row style={{
                          fontSize: 19,
                          fontWeight: 600,
                      }}>
                          {item.title}
                      </Row>
                      <Row>
                        Date: {item.date}
                      </Row>
                      <Row>
                        By: {item.copyright}
                      </Row>
                    </div>

                  </div>
                </List.Item>
              )}
            />
           </div>
        </Content>
      </Layout>
    </Layout>
  );
}

export default App;
