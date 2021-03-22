```
import React from "react";
import ReactDOM from "react-dom";
import ImageUploading from "react-images-uploading";

import "./styles.css";

function App() {
  const [images, setImages] = React.useState([]);
  const maxNumber = 69;
  const onChange = (imageList, addUpdateIndex) => {
    // data for submit
    console.log(imageList, addUpdateIndex);
    setImages(imageList);
  };

  return (
    <div className="App">
      <ImageUploading
        multiple
        value={images}
        onChange={onChange}
        maxNumber={maxNumber}
        dataURLKey="data_url"
      >
        {({
          imageList,
          onImageUpload,
          onImageRemoveAll,
          onImageUpdate,
          onImageRemove,
          isDragging,
          dragProps
        }) => (
          // write your building UI
          <div className="upload__image-wrapper">
            <button
              style={isDragging ? { color: "red" } : null}
              onClick={onImageUpload}
              {...dragProps}
            >
              Click or Drop here
            </button>
            &nbsp;
            <button onClick={onImageRemoveAll}>Remove all images</button>
            {imageList.map((image, index) => (
              <div key={index} className="image-item">
                <img src={image.data_url} alt="" width="100" />
                <div className="image-item__btn-wrapper">
                  <button onClick={() => onImageUpdate(index)}>Update</button>
                  <button onClick={() => onImageRemove(index)}>Remove</button>
                </div>
              </div>
            ))}
          </div>
        )}
      </ImageUploading>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
```

> img uploader



```
import React, { useState } from "react";
import axios from "axios";
import "./register.css";
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';

const BASE_URL = "http://localhost:8080";
const titleInputRef = React.createRef();
const storyInputRef = React.createRef();
export default function Register() {
  const [content, setContent] = useState("");
  const [imgBase64, setImgBase64] = useState("");
  const [imgFile, setImgFile] = useState(null);

  const [uploadedImg, setUploadedImg] = useState({
    fileName: "",
    filePath: "",
  });
  const onChange = e => {
    const reader = new FileReader();
    reader.onloadend = () => {
      const base64 = reader.result;
      if (base64) {
        setImgBase64(base64.toString());
      }
    };
    if (e.target.files[0]) {
      reader.readAsDataURL(e.target.files[0]);
      setImgFile(e.target.files[0]);
      // console.log(e.target.files[0])
    }
    setContent(e.target.files[0]);
    // console.log(content);
  };
  const onSubmit = e => {
    e.preventDefault();
    const formData = new FormData();
    const title = titleInputRef.current.value;
    const story = storyInputRef.current.value;
    formData.append("img", content);
    formData.append("title", title);
    formData.append("story", story);
    titleInputRef.current.value = '';
    storyInputRef.current.value = '';
    console.log(formData);
    axios
      .post(BASE_URL, formData)
      .then(res => {
        const { fileName } = res.data;
        // console.log(res)
        setUploadedImg({ fileName, filePath: `${BASE_URL}/img/${fileName}` });
        alert("The file is successfully uploaded");
      })
      .catch(err => {
        console.error(err);
      });
  };
  return (
    <>
      <h1>새글 작성 PAGE</h1>
  <form onSubmit={onSubmit} className="greybox">
       <Container className="contaniner-background" maxWidth="sm">
        {uploadedImg ? (
          <>
            <img src= {imgBase64} width="250" height="250" alt=""/>
            {/* <img width="250" height="250" src={uploadedImg.filePath} alt="" /> */}
            {/* <h3>{uploadedImg.fileName}</h3> */}
            <div className="input-center">
       제목 : <input ref={titleInputRef} type="text" placeholder="제목 입력" id=""/><br/>
       본문 : <input ref={storyInputRef} type="text" placeholder="본문을 입력하세요"/>
       </div>

          </>
        ) : (
          ""
        )}

        <input type="file" name="imgFile" onChange={onChange} /><br/>
        <div className="button-positon">
        <button className="button-mg" type="submit">upload</button>
        </div>
        </Container>

      </form>
    </>
  );
}

```

> 전버전

```
import React from "react";
import ImageUploading from "react-images-uploading";
import upload from "../../assets/upload.PNG";
// import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import "./Create.css";
import axios from 'axios';

export default function Create() {
  const titleRef = React.createRef();
  const contextRef = React.createRef();
  const [images, setImages] = React.useState([]);
  const maxNumber = 69;
  const files = new FormData();
  const onlistChange = (imageList, addUpdateIndex) => {
    // data for submit
    // console.log(imageList, addUpdateIndex);
    setImages(imageList);
    console.log(images);
    console.log(imageList);
    // console.log(imageList, addUpdateIndex);
    for (const image of imageList) {
      files.append('files', image.file);
    }
    // axios 통신하는 위치
  };
  const onSubmit = (event) => {
    event.preventDefault();
    console.log(images);
    // console.log(imageList);
    const request = {
      title: titleRef.current.value,
      context: contextRef.current.value,
    };
    files.append('title', request.title);
    files.append('context', request.context);
    axios.post("/api/board/create", files, {})
      .then(response => console.log(response))
      .then(result => console.log(result))
      .catch(error => console.error('error', error));
    setImages([]);
    titleRef.current.value = '';
    contextRef.current.value = '';
  };
  return (
    <form onSubmit={onSubmit}>
      <ImageUploading
        multiple
        value={images}
        onChange={onlistChange}
        maxNumber={maxNumber}
        dataURLKey="data_url"
      >
        {({
          imageList,
          onImageUpload,
          onImageRemoveAll,
          onImageUpdate,
          onImageRemove,
          isDragging,
          dragProps,
        }) => (
          // write your building UI
          <div
          {...dragProps}>
            <div
              className="uploadimg"
              onClick={onImageUpload}
            >
              <img src={upload} alt="왜"/>
            </div>
            <div onClick={onImageRemoveAll}>RESET</div>
            &nbsp;
            <Grid container spacing={1}>
            {images.map((image, index) => (
              <Grid key={index} className="image-item">
               <img src={image.data_url} alt="어디써" width="100" />
                <div className="">
                  <div onClick={() => onImageUpdate(index)}><i className="fas fa-pen color-yellow"></i></div>
                  <div onClick={() => onImageRemove(index)}><i className="fas fa-times-circle color-red"></i></div>
                </div>
              </Grid>
            ))}
            </Grid>
          </div>
        )}
      </ImageUploading>
      <div className="text-div">
          <input ref={titleRef} type="text" placeholder="제목을 입력하세요"/>
          <input ref={contextRef} type="text" placeholder="내용을 입력하세요"/>

      </div>
      <button>생성하기</button>
    </form>
  );
}

```

수정전

> 자바스크립 수정

```
/* eslint-disable no-loop-func */
import React, {useState} from "react";
import ImageUploading from "react-images-uploading";
import upload from "../../assets/upload.PNG";
// import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import "./Create.css";
import axios from 'axios';

export default function Create() {
    const [content, setContent] = useState("");
  const [imgBase64, setImgBase64] = useState("");
  const [imgFile, setImgFile] = useState(null);
  const [uploadedImg, setUploadedImg] = useState({
    fileName: "",
    filePath: "",
  });
    const [addDiary, setAddDiary] = useState({date: null, content: null, images: []});
    const [image, setImage] = useState([]);
    const selectImage = (e) => {
        console.log(e.target.value);
    };
    const onChange = e => {
        const reader = new FileReader();
        reader.onloadend = () => {
          const base64 = reader.result;
          if (base64) {
            setImgBase64(base64.toString());
          }
        };
        if (e.target.files[0]) {
          reader.readAsDataURL(e.target.files[0]);
          setImgFile(e.target.files[0]);
        }
      };
    const deleteImage = (name, e) => {
        const remainingImage = image.filter(img => img.name !== name);
        setImage(remainingImage);
        const remainingImageState = addDiary.images.filter(img =>
            img.name !== name);
        setAddDiary({...addDiary, images: remainingImageState });
    };

    const pickImage = (e) => {
        console.log(e, 'e obj');
        const limitImages = e.target.files.length;
        let count = 0;
        const images = [];
        for (const file of e.target.files) {
          const reader = new FileReader();
          reader.onload = (e) => {
            images.push({ url: URL.createObjectURL(file), name: file.name });
            count++;

            if (count === limitImages) {
              // here all images are loaded, so update the state
              setImage(images);
              setAddDiary({ ...addDiary, images: addDiary.images.concat(images)});
            }
          reader.readAsDataURL(file);
            };
        }
 };


  return (
      <>
       <h1>새글 작성 PAGE</h1>
  <form className="greybox">
       <div>
        {uploadedImg ? (
          <>
            <img src= {imgBase64} width="250" height="250" alt=""/>
            {/* <img width="250" height="250" src={uploadedImg.filePath} alt="" /> */}
            {/* <h3>{uploadedImg.fileName}</h3> */}
            <div className="input-center">
       </div>

          </>
        ) : (
          ""
        )}

        <input type="file" name="imgFile" onChange={onChange} /><br/>
        <div className="button-positon">
        <button className="button-mg" type="submit">upload</button>
        </div>
        </div>

      </form>
    <div className="md-form mb-5">
  <input type="file" id="form29" name='images' onChange={e => pickImage(e)} className="form-control validate" multiple hidden id="file-picker" />
  <button className="btn btn-outline-dark btn-sm" onClick={e => selectImage(e)}>
    <label id={'file-picker'}>
      Pick Image
    </label>
  </button>
</div>
          <div className="row text-center">
              {image.length > 0 ?
              image.map(img => (
                <div className="col-md-4" key={img.name}>
                <img src={img} alt={img} className="img-fluid"/>
                <span style={{cursor: 'pointer'}}>
                <i class="far fa-trash-alt" onClick={e => deleteImage(img.name, e)}></i>
                </span>
              </div>
              )) : <p>No Images Picked</p>}
          </div>
    </>
  );
}

```



create.jsx

```
import React, { Component } from 'react';
import axios from 'axios';

export default class Createtest extends Component {
    fileObj = [];
    fileArray = [];
    images = [];
    titleRef = React.createRef();
    contextRef = React.createRef();
    constructor(props) {
        super(props);
        this.state = {
            file: [null],
        };
        this.uploadMultipleFiles = this.uploadMultipleFiles.bind(this);
        this.uploadFiles = this.uploadFiles.bind(this);
    }

    uploadMultipleFiles(e) {
        this.images.push(e.target.files);
        this.fileObj.push(e.target.files);
        for (let i = 0; i < this.fileObj[0].length; i++) {
            this.fileArray.push(URL.createObjectURL(this.fileObj[0][i]));
        }
        console.log(this.fileArray);
        this.setState({ file: this.fileArray});
        this.fileObj.pop();
    }

    uploadFiles(e) {
        e.preventDefault();
        const formData = new FormData();
        formData.append('title', this.titleRef.current.value);
        formData.append('context', this.contextRef.current.value);
        console.log(this.images);
        for (const image of this.images[0]) {
        formData.append('files', image);
        }
        // console.log(this.state.file);
        axios.post("/api/board/create", formData, {})
        .then(response => console.log(response))
        .then(result => console.log(result))
        .catch(error => console.error('error', error));
        this.titleRef.current.value = '';
        this.contextRef.current.value = '';
    }

    render() {
        return (
            <form onSubmit={this.uploadFiles}>
                <div className="form-group multi-preview">
                    {(this.fileArray || []).map(url => (
                        <img src={url} key={url} width="100px" height="100px" alt="..." />
                    ))}
                </div>

                <div className="form-group">
                    <input type="file" className="form-control" onChange={this.uploadMultipleFiles} multiple />
                        <input ref={this.titleRef} placeholder="제목을 입력하시오" type="text"/>
                        <input ref={this.contextRef} placeholder="내용을 입력하시오" type="text"/>
                </div>
                <button>Upload</button>
            </form >
        );
    }
}

```

