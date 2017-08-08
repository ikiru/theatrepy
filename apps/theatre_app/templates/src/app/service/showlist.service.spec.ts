import { TestBed, inject } from '@angular/core/testing';

import { ShowlistService } from './showlist.service';

describe('ShowlistService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ShowlistService]
    });
  });

  it('should be created', inject([ShowlistService], (service: ShowlistService) => {
    expect(service).toBeTruthy();
  }));
});
