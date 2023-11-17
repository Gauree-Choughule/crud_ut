import React, { useState } from 'react';
import axios from 'axios';

const CreateBookModal = ({ onClose, onBookCreated }) => {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:5000/books', {
        title,
        author,
      });

      if (response.status === 200) {
        // Book created successfully
        onBookCreated();
        onClose(); // Close the modal after creating the book
      }
    } catch (error) {
      console.error('Error creating book:', error);
    }
  };

  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={onClose}>&times;</span>
        <form onSubmit={handleSubmit}>
          <label style={{ paddingLeft: '30px', fontWeight: 'bold' }}>
            Title:
            <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} style={{marginBottom: '30px', marginLeft: '10px', padding: '5px', width: '300px' }} placeholder="Enter book title" />
          </label>
          <label style={{ paddingLeft: '30px', fontWeight: 'bold' }}>
            Author:
            <input type="text" value={author} onChange={(e) => setAuthor(e.target.value)} style={{ marginLeft: '10px', padding: '5px', width: '300px' }} placeholder="Enter author name" />
          </label>
          <button type="submit" style={{ marginLeft: '20px', marginRight: '20px', width: '100px', fontWeight: 'bold' }}>Create Book</button>
        </form>
      </div>
    </div>
  );
};

export default CreateBookModal;
