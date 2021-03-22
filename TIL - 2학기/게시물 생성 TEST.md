```
import React from "react";
import ImageUploading from "react-images-uploading";
import upload from "../../assets/upload.PNG";
// import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import styles from "./Create.css";
import axios from 'axios';

export default function Create() {
  const titleRef = React.createRef();
  const contextRef = React.createRef();
  const fileInputRef = React.createRef();
  const [images, setImages] = React.useState([]);
  // const [title, setTitle] = React.useState('');
  // const [context, setContent] = React.useState('');
  const maxNumber = 69;
  const onChange = (imageList, addUpdateIndex) => {
    // data for submit
    // console.log(imageList, addUpdateIndex);
    setImages(imageList);
    // axios 통신하는 위치
  };
  const onSubmit = (event) => {
    event.preventDefault();
    const request = {
      title: titleRef.current.value,
      context: contextRef.current.value,
      imageList: images,

    };
    console.log(fileInputRef.current.files);
    const files = {
      files: fileInputRef.current.files[0],
    };
    // console.log(request);

    axios.post("/api/board/createV2", request, files)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
    // axios.post('/api/board/createV2', request, files)
    //     .then(res => console.log(res.data));
    titleRef.current.value = '';
    contextRef.current.value = '';
    setImages('');
  };

  return (
    <form onSubmit={onSubmit}>
      
      <button>생성하기</button>
    </form>
  );
}

// const rootElement = document.getElementById("root");
// ReactDOM.render(<Create />, rootElement);

```

수정전!





```
import React from "react";
import ImageUploading from "react-images-uploading";
import upload from "../../assets/upload.PNG";
// import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import styles from "./Create.css";
import axios from 'axios';

export default function Create() {
  const titleRef = React.createRef();
  const contextRef = React.createRef();
  const [images, setImages] = React.useState([]);
  // const [title, setTitle] = React.useState('');
  // const [context, setContent] = React.useState('');
  const maxNumber = 69;
  const onChange = (e) => {
    setImages(e.target.files);
    console.log(e.target.files);
    // axios 통신하는 위치
  };
  const onSubmit = (event) => {
    event.preventDefault();
    const request = {
      title: titleRef.current.value,
      context: contextRef.current.value,
      // imageList: images,

    };
    const formData = new FormData();
    formData.append('title', titleRef.current.value);
    formData.append('context', contextRef.current.value);
    for (const image of images) {
      formData.append('files', image);
    }

    axios.post("/api/board/createV2", formData, {})
      .then(response => console.log(response))
      .then(result => console.log(result))
      .catch(error => console.error('error', error));
    titleRef.current.value = '';
    contextRef.current.value = '';
    setImages('');
  };

  return (
    <form onSubmit={onSubmit}>
          <div>

            <input type="file" multiple
              onChange={onChange}
            />
              <img src={upload} alt="왜"/>
            <div className="text-div">
              <input ref={titleRef} type="text" placeholder="제목을 입력하세요"/>
              <input ref={contextRef} type="text" placeholder="내용을 입력하세요"/>
            </div>
            {/* <Grid container spacing={1}>
            {images.map((image, index) => (
              <Grid key={index} className="image-item">
                <img src={image.data_url} alt="" width="100" />
              </Grid>
            ))}
            </Grid> */}
             <button>생성하기</button>
        </div>
    </form>
  );
}


```

```
되는 상태!
import React from "react";
import ImageUploading from "react-images-uploading";
import upload from "../../assets/upload.PNG";
// import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import styles from "./Create.css";
import axios from 'axios';

export default function Create() {
  const titleRef = React.createRef();
  const contextRef = React.createRef();
  const [images, setImages] = React.useState([]);
  // const [title, setTitle] = React.useState('');
  // const [context, setContent] = React.useState('');
  const maxNumber = 69;
  const onChange = (e) => {
    const files = e.target.files;
    setImages(files);
    console.log(files);
    // axios 통신하는 위치
  };
  const onSubmit = (event) => {
    event.preventDefault();
    const request = {
      title: titleRef.current.value,
      context: contextRef.current.value,
      // imageList: images,

    };
    console.log(request);
    const formData = new FormData();
    formData.append('title', request.title);
    formData.append('context', request.context);
    for (const image of images) {
      formData.append('files', image);
    }
    console.log(formData);
    // const config = {
    //   headers: {
    //     "content-type": "multipart/form-data",
    //   },
    // };

    axios.post("/api/board/createV2", formData, {})
      .then(response => console.log(response))
      .then(result => console.log(result))
      .catch(error => console.error('error', error));
    titleRef.current.value = '';
    contextRef.current.value = '';
    setImages('');
  };

  return (
    <form onSubmit={onSubmit} >
          <div>

            <input type="file" multiple
              onChange={onChange}
            />
              <img src={upload} alt="왜"/>
            <div className="text-div">
              <input ref={titleRef} type="text" placeholder="제목을 입력하세요"/>
              <textarea ref={contextRef} type="text" placeholder="내용을 입력하세요"/>
            </div>

             <button>생성하기</button>
        </div>
    </form>
  );
}


```

```
import React, { Component } from 'react';

export default class MultipleImageUploadComponent extends Component {

    fileObj = [];
    fileArray = [];

    constructor(props) {
        super(props)
        this.state = {
            file: [null]
        }
        this.uploadMultipleFiles = this.uploadMultipleFiles.bind(this)
        this.uploadFiles = this.uploadFiles.bind(this)
    }

    uploadMultipleFiles(e) {
        this.fileObj.push(e.target.files)
        for (let i = 0; i < this.fileObj[0].length; i++) {
            this.fileArray.push(URL.createObjectURL(this.fileObj[0][i]))
        }
        this.setState({ file: this.fileArray })
    }

    uploadFiles(e) {
        e.preventDefault()
        console.log(this.state.file)
    }

    render() {
        return (
            <form>
                <div className="form-group multi-preview">
                    {(this.fileArray || []).map(url => (
                        <img src={url} alt="..." />
                    ))}
                </div>

                <div className="form-group">
                    <input type="file" className="form-control" onChange={this.uploadMultipleFiles} multiple />
                </div>
                <button type="button" className="btn btn-danger btn-block" onClick={this.uploadFiles}>Upload</button>
            </form >
        )
    }
}
```

```
import React, { Component } from 'react';
import axios from 'axios';

export default class MultipleImageUploadComponent extends Component {
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
        console.log(this.file);
        this.setState({ file: this.fileArray});
    }

    uploadFiles(e) {
        e.preventDefault();
        const formData = new FormData();
        formData.append('title', this.titleRef.current.value);
        formData.append('context', this.contextRef.current.value);
        // console.log(this.titleRef.current.value, this.contextRef.current.value);
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
        // this.images([]);
    }

    render() {
        return (
            <form onSubmit={this.uploadFiles}>
                <div className="form-group multi-preview">
                    {(this.fileArray || []).map(url => (
                        <img src={url} width="100px" height="100px" alt="..." />
                    ))}
                </div>

                <div className="form-group">
                    <input type="file" className="form-control" onChange={this.uploadMultipleFiles} multiple />
                        <input ref={this.titleRef} placeholder="제목을 입력하시오" type="text"/>
                        <textarea ref={this.contextRef} placeholder="내용을 입력하시오" type="text"/>
                </div>
                <button>Upload</button>
            </form >
        );
    }
}

```

