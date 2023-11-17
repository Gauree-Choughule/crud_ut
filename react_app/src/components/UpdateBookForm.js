import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UpdateBookForm = ({ bookId, onUpdate, onClose, setUpdateBookId }) => {
  const [book, setBook] = useState(null);
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [updateSuccess, setUpdateSuccess] = useState(false);

  useEffect(() => {
    const fetchBook = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/books/${bookId}`);
        setBook(response.data);
        setTitle(response.data.title);
        setAuthor(response.data.author);
      } catch (error) {
        console.error('Error fetching book:', error);
      }
    };

    // Fetch the book data when the component mounts
    fetchBook();
  }, [bookId]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.patch(`http://localhost:5000/books/${bookId}`, {
        title,
        author,
      });

      // Trigger the parent component to refetch books
      onUpdate();
      setUpdateSuccess(true);
    } catch (error) {
      console.error('Error updating book:', error);
    }
  };

  const handleClose = () => {
    // Reset the form and close the modal
    setUpdateSuccess(false);
    onClose();
  };

  return (
    <div className="modal">
      <div className="modal-content">
      <span className="close" onClick={() => { onClose(); setUpdateBookId(null); }}>&times;</span>
        {updateSuccess ? (
          <p>Update successful! <span onClick={handleClose} style={{ cursor: 'pointer' }}>Close</span></p>
        ) : (
          <form onSubmit={handleSubmit}>
            {book && (
              <>
                <label style={{ paddingLeft: '30px', fontWeight: 'bold' }}>
                  Title:
                  <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} style={{ marginBottom: '30px', marginLeft: '10px', padding: '5px', width: '300px' }} />
                </label>
                <label style={{ paddingLeft: '30px', fontWeight: 'bold' }}>
                  Author:
                  <input type="text" value={author} onChange={(e) => setAuthor(e.target.value)} style={{ marginLeft: '10px', padding: '5px', width: '300px' }} />
                </label>
                <button type="submit" style={{ marginLeft: '20px', marginRight: '20px', width: '100px', fontWeight: 'bold' }}>Update Book</button>
              </>
            )}
          </form>
        )}
      </div>
    </div>
  );
};

export default UpdateBookForm;

