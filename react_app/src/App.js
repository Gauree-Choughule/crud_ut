import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UpdateBookForm from './components/UpdateBookForm.js';
import PageNotFound from './components/PageNotFound.js';
import DeleteConfirmationModal from './components/DeleteConfirmationModal.js';
import CreateBookModal from './components/CreateBookModal.js';
import './app.scss'

const App = () => {
  const [books, setBooks] = useState([]);
  const [bookCreated, setBookCreated] = useState(false);
  const [updateBookId, setUpdateBookId] = useState(null);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [deleteBookId, setDeleteBookId] = useState(null);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const recordsPerPage = 5; 
  const lastIndex = currentPage * recordsPerPage;
  const firstIndex = lastIndex - recordsPerPage;
  const records = books.slice(firstIndex, lastIndex);
  const npage = Math.ceil(books.length/recordsPerPage)
  const numbers = [...Array(npage+1).keys()].slice(1)


  useEffect(() => {
    // Fetch the books when the component mounts or when a new book is created
    fetchBooks();
  }, [bookCreated, showCreateModal, showDeleteModal]);

  const fetchBooks = async () => {
    try {
      const response = await axios.get('http://localhost:5000/books');
      console.log("resp: ", response);
      setBooks(response.data.books);
    } catch (error) {
      console.error('Error fetching books:', error);
    }
  };

  const handleBookCreated = () => {
    // Trigger a re-fetch of books when a new book is created
    setBookCreated(true);
    // Close the create modal after book is created
    setShowCreateModal(false);
  };

  const handleUpdateClick = (bookId) => {
    setUpdateBookId(bookId);
  };

  const showDeleteConfirmation = (bookId) => {
    setDeleteBookId(bookId);
    setShowDeleteModal(true);
  };
  
  const hideDeleteConfirmation = () => {
    setDeleteBookId(null);
    setShowDeleteModal(false);
  };

  const handleConfirmDelete = async () => {
    try {
      await axios.delete(`http://localhost:5000/books/${deleteBookId}`);
      // Update the state after successful deletion
      setBooks(books.filter((book) => book.id !== deleteBookId));
      hideDeleteConfirmation();
    } catch (error) {
      console.error('Error deleting book:', error);
    }
  };

  const handleDelete = (bookId) => {
    showDeleteConfirmation(bookId);
  };

  function prePage() {
    if (currentPage !== 1) {
      setCurrentPage(currentPage - 1);
    }
  }
  
  function changePage(id) {
    setCurrentPage(id);
  }
  
  function nextPage() {
    if (currentPage !== npage) {
      setCurrentPage(currentPage + 1);
    }
  }

  const Home = ({ books, fetchBooks, setUpdateBookId, handleBookCreated, setShowCreateModal, showCreateModal, handleUpdateClick, handleDelete, updateBookId, showDeleteModal, hideDeleteConfirmation, handleConfirmDelete }) => (
    <div>
      <h1>Book Management Application</h1>
      
      <button onClick={() => setShowCreateModal(true)} >Create new Book</button>
  
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Author</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {records.map((book) => (
            <tr key={book.id}>
              <td>{book.id}</td>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>
                <button onClick={() => handleUpdateClick(book.id)}>Update</button>
                <button onClick={() => handleDelete(book.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <nav>
        <ul className='pagination'>
          <li className='page-item'>
          <button className='page-link' onClick={prePage}>Prev</button>
          </li>
          { numbers.map((n, i) => (
            <li className={`page-item ${currentPage === n ? 'active' : ''}`} key={i}>
            <button className='page-link' onClick={() => changePage(n)}>{n}</button>       
          </li>
          ))}
          <li className='page-item'>
          <button className='page-link' onClick={nextPage}>Next</button>
          </li>
        </ul>
      </nav>
      
      {updateBookId && (<UpdateBookForm bookId={updateBookId} onUpdate={fetchBooks} onClose={() => setUpdateBookId(null)} setUpdateBookId={setUpdateBookId}/>)}
      {showCreateModal && <CreateBookModal onClose={() => setShowCreateModal(false)} onBookCreated={handleBookCreated} />}
      {showDeleteModal && (<DeleteConfirmationModal onCancel={hideDeleteConfirmation} onConfirm={handleConfirmDelete} />)}
    </div> 
  );
  
  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={<Home
            books={books}
            fetchBooks={fetchBooks}
            setUpdateBookId={setUpdateBookId}
            handleBookCreated={handleBookCreated}
            handleUpdateClick={handleUpdateClick}
            handleDelete={handleDelete}
            updateBookId={updateBookId}
            showDeleteModal={showDeleteModal}
            hideDeleteConfirmation={hideDeleteConfirmation}
            handleConfirmDelete={handleConfirmDelete}
            showCreateModal={showCreateModal} 
            setShowCreateModal={setShowCreateModal} 
          />}
        />
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </Router>
  );
};


export default App;


