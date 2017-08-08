import { TestBed, inject } from '@angular/core/testing';

import { TcatagoryService } from './tcatagory.service';

describe('TcatagoryService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TcatagoryService]
    });
  });

  it('should be created', inject([TcatagoryService], (service: TcatagoryService) => {
    expect(service).toBeTruthy();
  }));
});
