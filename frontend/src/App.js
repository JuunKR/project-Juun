import React from 'react'

const App = () =>{
  return(<>
    <nav>
      <Link to="./index.html">Home</Link>
      <Link tp="./blog_list.html">Blog</Link>
      <Link to="about_Ome.html">About Me</Link>
    </nav>
    <h1>첫번째 크기 헤드라인</h1>
    <h2>두 번째 크기 헤드라인</h2>
    <h3>세 번째 크기 헤드라인</h3>
    <h4>다섯 번째 크기 헤드라인</h4>
    <P>문단으 p로 쓰세요. p는 아마도 Paragraph의 앞글자를 따온 것이겠죠?</P>
    <Link to="https://www.google.com">Go to google</Link>
    <hr/>
    <img src="./images/stat_funky.jpg" width="600px"></img>
    </>
  )
}
export default App