```
import React, { Component } from 'react';
import SearchBar from "./SearchBar";
import axios from 'axios';
import './Create.css';
import {COUNTRIES} from './contries';
import SingleLineGridList from './Test';
// # 시작
const suggestions = COUNTRIES.map((country) => ({
  name: country,
}));
export default class Create extends Component {
    fileObj = [];
    fileArray = [];
    fileArrayFirst = '';
    images = [];
    titleRef = React.createRef();
    contextRef = React.createRef();
    constructor(props) {
        super(props);
        this.state = {
            hashtags: [null],
            focused: false,
            // input: '',
            file: [null],
            keyword: "",
            results: [],
            suggestions,
        };
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleInputKeyDown = this.handleInputKeyDown.bind(this);
        this.handleRemoveItem = this.handleRemoveItem.bind(this);
        this.uploadMultipleFiles = this.uploadMultipleFiles.bind(this);
        this.uploadFiles = this.uploadFiles.bind(this);
    }
    uploadMultipleFiles(e) {
        this.images = e.target.files;
        this.fileObj = e.target.files;
        for (let i = 0; i < this.fileObj.length; i++) {
            this.fileArray = [
            ...this.fileArray,
            {URL: URL.createObjectURL(this.fileObj[i]), id: i + Date.now(), Obj: this.fileObj[i]},
        ];
        }
        this.fileArrayFirst = this.fileArray[0].URL;
        this.setState({img: this.tileObj});
        console.log(this.fileArray);
        this.setState({ file: this.fileArray});
    }

    uploadFiles(e) {
        e.preventDefault();
        const formData = new FormData();
        formData.append('title', this.titleRef.current.value);
        formData.append('context', this.contextRef.current.value);
        formData.append('hashtags', this.state.hashtags);
        console.log(this.fileArray);
        for (const i of this.fileArray) {
        const img = i.Obj;
          formData.append('files', img);
        }
        // console.log(this.state.file);
        axios.post("/api/board/create", formData, {})
        .then(response => console.log(response))
        .then(result => console.log(result))
        .catch(error => console.error('error', error));
        this.titleRef.current.value = '';
        this.contextRef.current.value = '';
    }
    handleDelete(image) {
      console.log(this.fileArray);
      const fileArray = this.fileArray.filter(item =>
      item.id !== image.id);
      this.fileArray = fileArray;
      if (fileArray.length === 0) {
        this.fileArrayFirst = '';
      } else {
        this.fileArrayFirst = fileArray[0].URL;
      }
      this.setState({file: fileArray});
    }
    handleInputChange(evt) {
      this.setState({ input: evt.target.value });
    }

    handleInputKeyDown(evt) {
      if (evt.keyCode === 13) {
        const {value} = evt.target;
        evt.preventDefault();

        this.setState(state => ({
          hashtags: [...state.hashtags, value],
          keyword: '',
        }));
      }

      if (this.state.hashtags.length && evt.keyCode === 8 && !this.state.keyword.length) {
        this.setState(state => ({
          hashtags: state.hashtags.slice(0, state.hashtags.length - 1),
        }));
      }
    }
    handleRemoveItem(index) {
      return () => {
        this.setState(state => ({
          hashtags: state.hashtags.filter((item, i) => i !== index),
        }));
      };
    }
    // matchName = (name, keyword) => {
    //   const keyLen = keyword.length;
    //   name = name.toLowerCase().substring(0, keyLen);
    //   if (keyword === "") return false;
    //   return name === keyword.toLowerCase();
    // };

    onSearch = async text => {
      let stockData; let
data;
      try {
        // console.log(COUNTRIES);
        // stockData = await fetch(
        //   `https://financialmodelingprep.com/api/v3/search?query=${text}&limit=10&exchange=NASDAQ&apikey=abf4ef28fc7fd607624d9a8941444c42`,
        // );
        data = await stockData.json();
      } catch (err) {
        console.log(err.message);
      }
      // console.log(data);
      this.setState({ results: data });
    };

    updateField = (field, value) => {
      if (field === "keyword") this.onSearch(value);
      this.setState({ [field]: value });
    };
    render() {
      const {suggestions} = this.state;
      const { results, keyword } = this.state;
        return (
            <form onSubmit={this.uploadFiles}>
                <div className="form-group multi-preview">
                  {/* <SingleLineGridList fileArray={this.fileArray} */}
                  {/* Ondelete={(item) => this.handleDelete(item)}/> */}
                  <img src={this.fileArrayFirst} width="300px" height="300px" alt=""/>
                    {(this.fileArray || {}).map(item => (
                      <div item={item} key={item.id}>
                        <img item={item} src={item.URL} key={item.id} width="100px" height="100px" alt="..." />
                        <span onClick={() => this.handleDelete(item)}>삭제</span>
                      </div>
                    ))}

                </div>

                <div className="form-group">
                    <input type="file" className="form-control" onChange={this.uploadMultipleFiles} multiple />
                        <input ref={this.titleRef} placeholder="제목을 입력하시오" type="text"/>
                        <input ref={this.contextRef} placeholder="내용을 입력하시오" type="text"/>

                </div>
                <div className="input-tag">
                <ul className="input-tag__tags">
                    {(this.state.hashtags).map((item, i) =>
                      <li className="input-tag__tags__li" key={i} onClick={this.handleRemoveItem(i)}>
                        {item}
                        <span>+</span>
                      </li>,
                    )}
                    </ul>
                    <SearchBar
                    suggestions={suggestions}
                    results={suggestions}
                    keyword={keyword}
                    updateField={this.updateField}
                    onhandleInputKeyDown={this.handleInputKeyDown}
                    onhandleInputChange={this.handleInputChange}

                  />
                  </div>
              <button>Upload</button>
            </form >
        );
    }
}

```

```

.container {
}
.header {
  width: 100%;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin:3px;
  font-size: 3rem;
  background-color: rgba(14, 1, 13, 0.2)
}
.form-card {
  margin: 1em;
  display : flex;
  justify-content: space-between;
  width:100%;
  height: 800px;
  border: 3px solid black;
  background-color: violet;
  box-sizing: border-box;
}
.img-card {
  position: absolute;
  margin-right : 500px;
  margin-top:200px;
  width: 30%;
  height:50%;
  /* box-sizing: border-box; */
  /* border: 10px solid black; */
  /* float: left; */
}
.img-list {
  position: relative;
  display: flex;
  flex-wrap: wrap;
}
.img-able-delete{
    display : flex;
    position: relative;
    align-items: center;
    border: 1px solid lightgrey;
    cursor:pointer;
    transition: transform 250ms ease-in;
    -webkit-box-shadow: 13px 7px 9px 10px rgba(206,206,206,0.93); 
box-shadow: 13px 7px 9px 10px rgba(206,206,206,0.93);
  /* border: 4px solid black; */
}
.img-able-delete:hover {
  transform:scale(1.12);
}
.first-img{
  /* border: 6px solid black; */
}
.text-card {
  position: absolute;
  padding-top:200px;
  width: 30%;
  height:50%;
  
  margin-left : 500px;
  /* display: flex; */
  /* float:right; */
  /* justify-content: flex-end; */
  box-sizing: border-box;
  /* border: 3px solid black; */
}
input {
  display : inline;
}
.title-form{
  
}

.imageupload {
    width: 100vw;
    height: 100vh;
}

.imageupload.active {
    width: 100vw;
    height: 100vh;
    background-color:gray;
    opacity: 0.9;

}
.input-tag {
    background: white;
    /* border: 1px solid #d6d6d6; */
    border-radius: 2px;
    display: flex;
    flex-wrap: wrap;
    padding: 5px 5px 0;
  }
  
  .input-tag input {
    border: none;
    width: 100%;
  }
  
  .input-tag__tags {
    display: inline-flex;
    flex-wrap: wrap;
    margin: 0;
    padding: 0;
    width: 100%;
  }
  
  .input-tag__tags li {
    align-items: center;
    background: #85A3BF;
    border-radius: 2px;
    color: white;
    display: flex;
    font-weight: 300;
    list-style: none;
    margin-bottom: 5px;
    margin-right: 5px;
    padding: 5px 10px;
  }
  
  .input-tag__tags li span {
    align-items: center;
    appearance: none;
    background: #333333;
    border: none;
    border-radius: 50%;
    color: white;
    cursor: pointer;
    display: inline-flex;
    font-size: 12px;
    height: 15px;
    justify-content: center;
    line-height: 0;
    margin-left: 8px;
    padding: 0;
    transform: rotate(45deg);
    width: 15px;
  }
  
  .input-tag__tags li.input-tag__tags__input {
    background: none;
    flex-grow: 1;
    padding: 0;
  }
  .input-tag__tags li.input-tag__tags__input {
    background: none;
    flex-grow: 1;
    padding: 0;
  }
  .ButtonDeleteColorRed{
    color: red;
  }
  /* .MuiGridListTile-imgFullWidth{
    top: 50% !important;
    width:100px !important;
    position: relative !important;
    transform: translateY(-50%) !important;
  }

  .MuiGridList-root {
    display: flex !important;
    padding: 0 !important;
    flex-wrap: wrap !important;
    list-style: none !important;
    overflow-y: auto !important;
  } */
  .fileArray{
    display: flex;
  }
.fileArray div {
  width: 100px;
  height: 100px;
  display: none;
}
.fileArray :first-child {
  width: 300px;
  height: 300px;
  /* display: none; */
 }


```

```
import React, { Component } from 'react';
import SearchBar from "./SearchBar";
import axios from 'axios';
import './Create.css';
import {COUNTRIES} from './contries';
import SingleLineGridList from './Test';
// # 시작
const suggestions = COUNTRIES.map((country) => ({
  name: country,
}));
export default class Create extends Component {
    fileObj = [];
    fileArray = [];
    fileArrayFirst = '';
    images = [];
    titleRef = React.createRef();
    contextRef = React.createRef();
    constructor(props) {
        super(props);
        this.state = {
            hashtags: [null],
            focused: false,
            // input: '',
            file: [null],
            keyword: "",
            results: [],
            suggestions,
        };
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleInputKeyDown = this.handleInputKeyDown.bind(this);
        this.handleRemoveItem = this.handleRemoveItem.bind(this);
        this.uploadMultipleFiles = this.uploadMultipleFiles.bind(this);
        this.uploadFiles = this.uploadFiles.bind(this);
    }
    uploadMultipleFiles(e) {
        this.images = e.target.files;
        this.fileObj = e.target.files;
        for (let i = 0; i < this.fileObj.length; i++) {
            this.fileArray = [
            ...this.fileArray,
            {URL: URL.createObjectURL(this.fileObj[i]), id: i + Date.now(), Obj: this.fileObj[i]},
        ];
        }
        this.fileArrayFirst = this.fileArray[0].URL;
        this.setState({img: this.tileObj});
        console.log(this.fileArray);
        this.setState({ file: this.fileArray});
    }

    uploadFiles(e) {
        e.preventDefault();
        const profileId = localStorage.getItem('profileId');
        console.log(profileId);
        const formData = new FormData();
        formData.append('profileId', profileId);
        formData.append('title', this.titleRef.current.value);
        formData.append('context', this.contextRef.current.value);
        formData.append('hashtags', this.state.hashtags);
        console.log(this.fileArray);
        for (const i of this.fileArray) {
        const img = i.Obj;
          formData.append('files', img);
        }
        // console.log(this.state.file);
        axios.post("/api/board/create", formData, {})
        .then(response => console.log(response))
        .then(result => console.log(result))
        .catch(error => console.error('error', error));
        this.titleRef.current.value = '';
        this.contextRef.current.value = '';
    }
    handleDelete(image) {
      console.log(this.fileArray);
      const fileArray = this.fileArray.filter(item =>
      item.id !== image.id);
      this.fileArray = fileArray;
      if (fileArray.length === 0) {
        this.fileArrayFirst = '';
      } else {
        this.fileArrayFirst = fileArray[0].URL;
      }
      this.setState({file: fileArray});
    }
    handleInputChange(evt) {
      this.setState({ input: evt.target.value });
    }

    handleInputKeyDown(evt) {
      if (evt.keyCode === 13) {
        const {value} = evt.target;
        evt.preventDefault();

        this.setState(state => ({
          hashtags: [...state.hashtags, value],
          keyword: '',
        }));
      }

      if (this.state.hashtags.length && evt.keyCode === 8 && !this.state.keyword.length) {
        this.setState(state => ({
          hashtags: state.hashtags.slice(0, state.hashtags.length - 1),
        }));
      }
    }
    handleRemoveItem(index) {
      return () => {
        this.setState(state => ({
          hashtags: state.hashtags.filter((item, i) => i !== index),
        }));
      };
    }
    // matchName = (name, keyword) => {
    //   const keyLen = keyword.length;
    //   name = name.toLowerCase().substring(0, keyLen);
    //   if (keyword === "") return false;
    //   return name === keyword.toLowerCase();
    // };

    onSearch = async text => {
      let stockData; let
data;
      try {
        // console.log(COUNTRIES);
        // stockData = await fetch(
        //   `https://financialmodelingprep.com/api/v3/search?query=${text}&limit=10&exchange=NASDAQ&apikey=abf4ef28fc7fd607624d9a8941444c42`,
        // );
        // data = await stockData.json();
      } catch (err) {
        console.log(err.message);
      }
      // console.log(data);
      // this.setState({ results: data });
    };

    updateField = (field, value) => {
      if (field === "keyword") this.onSearch(value);
      this.setState({ [field]: value });
    };
    render() {
      const {suggestions} = this.state;
      const { results, keyword } = this.state;
        return (
            <div className="contaniner">
            <form onSubmit={this.uploadFiles} className="form-card">
            <header className="header"> 글 작성하기</header>
              <div className="img-card">
                <div className="img-list">
                  {/* <SingleLineGridList fileArray={this.fileArray} */}
                  {/* Ondelete={(item) => this.handleDelete(item)}/> */}
                    {(this.fileArray || {}).map(item => (
                      <li item={item} key={item.id} className="img-able-delete">
                        <img item={item} src={item.URL} key={item.id} width="100px" height="100px" alt="..." />
                        <span onClick={() => this.handleDelete(item)}>삭제</span>
                      </li>

                    ))}
                </div>
                <div className="first-img">
                  <img src={this.fileArrayFirst} width="300px" height="300px" alt=""/>
                </div>
                <input type="file" className="form-control" onChange={this.uploadMultipleFiles} multiple />
              </div>
{/* ---------------------------------------------------------------------------------------------------- */}

                <div className="text-card">
                  <div className="title-form">
                    <input ref={this.titleRef} placeholder="제목을 입력하시오" type="text"/>
                    <input ref={this.contextRef} placeholder="내용을 입력하시오" type="text"/>
                  </div>

                  <div className="input-tag">
                    <ul className="input-tag__tags">
                        {(this.state.hashtags).map((item, i) =>
                          <li className="input-tag__tags__li" key={i} onClick={this.handleRemoveItem(i)}>
                            {item}
                            <span>+</span>
                          </li>,
                        )}
                    </ul>
                      {/* <SearchBar
                      suggestions={suggestions}
                      results={suggestions}
                      keyword={keyword}
                      updateField={this.updateField}
                      onhandleInputKeyDown={this.handleInputKeyDown}
                      onhandleInputChange={this.handleInputChange}

                    /> */}
                  </div>
                </div>
              <button>Upload</button>
            </form >
          </div>
        );
    }
}

```

