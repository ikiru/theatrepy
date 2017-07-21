import { TheaterangPage } from './app.po';

describe('theaterang App', () => {
  let page: TheaterangPage;

  beforeEach(() => {
    page = new TheaterangPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
