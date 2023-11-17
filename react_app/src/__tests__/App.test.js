// App.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import axios from 'axios';
import App from '../App';

jest.mock('axios');

const mockedBooks = [
  { id: 1, title: 'Akbarnama', author: 'Abul Fazl' }
];

describe('App Component - GET Method', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('fetches books and displays them', async () => {
    // Mock the axios get method to resolve with mocked data
    axios.get.mockResolvedValueOnce({ data: { books: mockedBooks } });

    render(<App />);

    // Check if books are displayed
    mockedBooks.forEach((book) => {
      expect(screen.getByText(book.title)).toBeInTheDocument();
      expect(screen.getByText(book.author)).toBeInTheDocument();
    });
  });
});

