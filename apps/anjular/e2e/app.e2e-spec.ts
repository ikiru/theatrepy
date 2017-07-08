import { AnjularPage } from './app.po';

describe('anjular App', () => {
  let page: AnjularPage;

  beforeEach(() => {
    page = new AnjularPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
